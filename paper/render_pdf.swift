// Render every page using macOS PDFKit; no package installation required.
import AppKit
import Foundation
import PDFKit

guard CommandLine.arguments.count == 3 else {
    fatalError("usage: swift render_pdf.swift input.pdf output-directory")
}
let inputURL = URL(fileURLWithPath: CommandLine.arguments[1])
let outputURL = URL(fileURLWithPath: CommandLine.arguments[2], isDirectory: true)
guard let document = PDFDocument(url: inputURL) else {
    fatalError("cannot open PDF")
}
try FileManager.default.createDirectory(at: outputURL, withIntermediateDirectories: true)
for index in 0..<document.pageCount {
    guard let page = document.page(at: index) else { fatalError("missing page") }
    let bounds = page.bounds(for: .mediaBox)
    let size = NSSize(width: 1100, height: 1100 * bounds.height / bounds.width)
    let preview = page.thumbnail(of: size, for: .mediaBox)
    var proposed = NSRect(origin: .zero, size: preview.size)
    guard let cg = preview.cgImage(forProposedRect: &proposed, context: nil, hints: nil),
          let png = NSBitmapImageRep(cgImage: cg).representation(using: .png, properties: [:])
    else { fatalError("cannot render page") }
    let destination = outputURL.appendingPathComponent(String(format: "page-%02d.png", index + 1))
    try png.write(to: destination, options: .atomic)
    print("rendered \(destination.path)")
}
print("pages: \(document.pageCount)")
