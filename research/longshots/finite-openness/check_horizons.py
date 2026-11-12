#!/usr/bin/env python3
"""Verify the session numbers for 'finite openness' in flat Lambda-CDM.

Standard integrals (flat, a0 = 1, Omega_L = 1 - Omega_m, E(z) = sqrt(Om (1+z)^3 + OL)):

  particle horizon now      Xp = (c/H0) * int_0^inf dz / E(z)
  event horizon now         Xe = (c/H0) * int_1^inf da / (a^2 E(a))
  ultimate particle horizon Xu = Xp + Xe            (= int_0^inf c dt / a(t), full time)
  age now                   t0 = (1/H0) * int_0^1 a da / E(a)

Well-conditioned substitutions (remove the a^{-1/2} integrable singularity):

  Xp/(c/H0) = int_0^1 2 dx / sqrt(Om + OL x^6)         (a = x^2)
  Xe/(c/H0) = int_0^1 dx  / sqrt(Om x^3 + OL)          (a = 1/x)
  t0 H0     = int_0^1 2 x^6 dx / sqrt(Om + OL x^6)     (a = x^2)

Cross-checks:
  (i) independent z-integral route for Xp (substitution u = x^2 on the far tail;
      analytic tail beyond z = 1e6 is < 1e-8).
  (ii) consistency z_eh: chi(z_eh) = Xe, i.e. light we emit now from z > z_eh
       never reaches us (published ballpark 1.7-1.9).
  (iii) published anchors: age ~13.8 Gyr; particle horizon ~46 Gly; and the
        maximum comoving radius of our past light cone (Davis & Lineweaver 2004,
        their params recomputed here, quoted by them as ~63 Gly - checked in RESULT.md).
  (iv) Simpson at two resolutions (dimensionless, must agree to ~1e-12 relative).

Only the Python standard library is used. Run: python3 check_horizons.py
"""
import math

C_KMS = 299792.458           # speed of light km/s
MPC_TO_GLY = 3.261563777e-3  # 1 Mpc in Gly (Julian years; 1 pc = 3.261563777 ly)

OM, OL = 0.315, 0.685        # flat, h = 0.674 -> H0 below
H0 = 67.4                    # km/s/Mpc
C_OVER_H0_GLY = C_KMS / H0 * MPC_TO_GLY
H0_INV_GYR = 977.81414 / H0  # 1/H0 in Gyr for H0 in km/s/Mpc (9.7781414 h^-1 Gyr)


def simpson(f, lo, hi, n=2 ** 14):
    """Composite Simpson on [lo, hi] with n even subintervals."""
    if n % 2:
        n += 1
    h = (hi - lo) / n
    s = f(lo) + f(hi)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(lo + i * h)
    return s * h / 3.0


def E_of_z(z):
    return math.sqrt(OM * (1.0 + z) ** 3 + OL)


def xp_dimensionless():          # int_0^1 2 dx / sqrt(Om + OL x^6)
    return simpson(lambda x: 2.0 / math.sqrt(OM + OL * x ** 6), 0.0, 1.0, 2 ** 14)


def xe_dimensionless():          # int_0^1 dx / sqrt(Om x^3 + OL)
    return simpson(lambda x: 1.0 / math.sqrt(OM * x ** 3 + OL), 0.0, 1.0, 2 ** 14)


def t0_dimensionless():          # dt = da/(aH): int_0^1 2 x^2 dx / sqrt(Om + OL x^6)
    return simpson(lambda x: 2.0 * x ** 2 / math.sqrt(OM + OL * x ** 6), 0.0, 1.0, 2 ** 14)


OR = 9.2e-5                     # Omega_r incl. massless neutrinos (h=0.674); radiation
                                # matters only at z >~ 50, i.e. only for Xp


def xp_rad_dimensionless():      # Xp with radiation: int_0^1 da/sqrt(Or + Om a + OL a^4),
    return simpson(              # then a = x^2 -> int_0^1 2x dx / sqrt(Or + Om x^2 + OL x^8)
        lambda x: 2.0 * x / math.sqrt(OR + OM * x ** 2 + OL * x ** 8), 0.0, 1.0, 2 ** 14)


def xp_redshift_route():         # independent route: int_0^inf dz / E(z)
    # z in [0, 10] directly; [10, inf) via z = 10/x^2 (integrand -> const, smooth at x->0):
    # dz = -20 dx/x^3, so [10,inf) -> int_0^1 20/(x^3 E(10/x^2)) dx.
    part1 = simpson(lambda z: 1.0 / E_of_z(z), 0.0, 10.0, 2 ** 13)
    limit_p2 = 20.0 / (math.sqrt(OM) * 10.0 ** 1.5)  # x -> 0 limit of the part2 integrand
    part2 = simpson(lambda x: limit_p2 if x == 0 else 20.0 / (x ** 3 * E_of_z(10.0 / (x * x))),
                    0.0, 1.0, 2 ** 14)
    # tail beyond z = 10/eps: eps -> 0 limit of integrand is finite const, tail ~ 0.11,
    # so this covers [10, inf) up to O(1e-7).
    return part1 + part2


def chi_of_z(z):                 # comoving distance to z, in units of c/H0
    return simpson(lambda zz: 1.0 / E_of_z(zz), 0.0, z, 2 ** 13)


def main():
    xp_gly = C_OVER_H0_GLY * xp_dimensionless()
    xe_gly = C_OVER_H0_GLY * xe_dimensionless()
    xu_gly = xp_gly + xe_gly
    t0_gyr = H0_INV_GYR * t0_dimensionless()

    print(f"Omega_m={OM}  Omega_L={OL}  h={H0 / 100:.3f}  (flat)")
    print(f"c/H0 = {C_KMS / H0:.1f} Mpc = {C_OVER_H0_GLY:.3f} Gly")
    print(f"particle horizon now      Xp = {xp_gly:.2f} Gly   (dimless {xp_dimensionless():.6f})")
    print(f"event horizon now         Xe = {xe_gly:.2f} Gly   (dimless {xe_dimensionless():.6f})")
    print(f"ultimate particle horizon Xu = {xu_gly:.2f} Gly")
    print(f"age now                   t0 = {t0_gyr:.3f} Gyr   (anchor ~13.8 Gyr)")
    print()
    xp_rad_gly = C_OVER_H0_GLY * xp_rad_dimensionless()
    print(f"Xp with radiation (Or={OR}) = {xp_rad_gly:.2f} Gly "
          f"(dimless {xp_rad_dimensionless():.6f})")
    print()
    frac_past = (xp_gly / xu_gly) ** 3
    frac_eh = (xe_gly / xp_gly) ** 3
    print(f"(Xp/Xu)^3 = {frac_past:.4f}  -> {100 * frac_past:.1f}% of ultimately visible")
    print(f"            comoving volume already in our past cone   (claim: ~40%)")
    print(f"(Xe/Xp)^3 = {frac_eh:.4f}  -> {100 * frac_eh:.2f}% of presently visible")
    print(f"            comoving volume inside our event horizon   (claim: 4.7%)")
    print()
    # independent z-route for Xp
    xp_alt = C_OVER_H0_GLY * xp_redshift_route()
    print(f"cross-check Xp via z-integral        = {xp_alt:.4f} Gly "
          f"(rel diff {abs(xp_alt - xp_gly) / xp_gly:.2e})")
    # Simpson resolution check (dimensionless vs dimensionless)
    xp_hi = simpson(lambda x: 2.0 / math.sqrt(OM + OL * x ** 6), 0.0, 1.0, 2 ** 16)
    xe_hi = simpson(lambda x: 1.0 / math.sqrt(OM * x ** 3 + OL), 0.0, 1.0, 2 ** 16)
    print(f"cross-check resolution 2^14 vs 2^16  = rel diff "
          f"{abs(xp_hi - xp_dimensionless()) / xp_dimensionless():.2e}, "
          f"{abs(xe_hi - xe_dimensionless()) / xe_dimensionless():.2e}")
    # z_eh: sources whose light emitted NOW never reaches us
    target = xe_dimensionless()
    lo, hi = 0.0, 10.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if chi_of_z(mid) < target:
            lo = mid
        else:
            hi = mid
    print(f"z_eh (light emitted now never arrives if z > z_eh) = {0.5 * (lo + hi):.3f}"
          f"   (published ballpark: ~1.7-1.9)")
    # Davis & Lineweaver-epoch parameters (Om=0.3, OL=0.7, H0=70) for comparison
    print()
    print("Davis & Lineweaver 2004 anchor (their params Om=0.3, OL=0.7, H0=70):")
    om2, ol2, ch2 = 0.3, 0.7, C_KMS / 70.0 * MPC_TO_GLY
    xp2 = ch2 * simpson(lambda x: 2.0 / math.sqrt(om2 + ol2 * x ** 6), 0.0, 1.0, 2 ** 14)
    xe2 = ch2 * simpson(lambda x: 1.0 / math.sqrt(om2 * x ** 3 + ol2), 0.0, 1.0, 2 ** 14)
    print(f"  Xp={xp2:.1f} Gly  Xe={xe2:.1f} Gly  Xu={xp2 + xe2:.1f} Gly"
          f"  (D&L Sec. 6 discusses ~63 Gly maximum; exact wording checked in RESULT.md)")
    # radiation-included volume fraction, for the report
    xu_rad_gly = xp_rad_gly + xe_gly
    print(f"with radiation: Xu={xu_rad_gly:.2f} Gly, "
          f"(Xp/Xu)^3={100 * (xp_rad_gly / xu_rad_gly) ** 3:.1f}%, "
          f"(Xe/Xp)^3={100 * (xe_gly / xp_rad_gly) ** 3:.2f}%")


if __name__ == "__main__":
    main()
