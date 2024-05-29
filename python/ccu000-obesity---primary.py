# Angela Wood, Rachel Denholm, Sam Hollings, Jennifer Cooper, Samantha Ip, Venexia Walker, Spiros Denaxas, Ashley Akbari, Amitava Banerjee, William Whiteley, Alvina Lai, Jonathan Sterne, Cathie Sudlow, CVD-COVID-UK consortium, 2024.

import sys, csv, re

codes = [{"code":"296526005","system":"snomedct"},{"code":"170807005","system":"snomedct"},{"code":"722051004","system":"snomedct"},{"code":"238134004","system":"snomedct"},{"code":"170797005","system":"snomedct"},{"code":"190965006","system":"snomedct"},{"code":"268551005","system":"snomedct"},{"code":"294493008","system":"snomedct"},{"code":"248311001","system":"snomedct"},{"code":"238136002","system":"snomedct"},{"code":"415530009","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu000-obesity-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu000-obesity---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu000-obesity---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu000-obesity---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
