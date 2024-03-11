# Duplex Scanner Document Stitch

### Usage

For DCP-L2640DW scanner, you can use the auto scan to scan a large number of documents at once. This spits out the stack of documents upside down and in reverse order. Thus if you take the same stack as-is and put it back into the feeder it will then scan all the backs of the documents too. This script simply stitches them all together so the resultant pdf has the backs of a page following the fronts.

```bash
alias duplexscan
duplexscan=/Users/barnabasvizy/projects/scanner-duplex-stitching/scanner-duplex-stitching.py

duplexscan /Users/barnabasvizy/local_documents/Scan2024-03-10_220217.pdf output.pdf
Input path: /Users/barnabasvizy/local_documents/Scan2024-03-10_220217.pdf
Output path: output.pdf
Pages found: 16
Done!
```