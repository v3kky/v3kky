#imports
import os
import argparse
import datetime

#argparse
parser = argparse.ArgumentParser(description='Script voor het verwerken van backup logfiles.')
parser.add_argument("-s", "--source", default="C:\BackupLogs\In",
help ="Source directory die de backupfiles bevat.")
parser.add_argument("-t", "--target", default="C:\BackupLogs\Out",
help ="Target directory waar het eindrapport wordt weggeschreven.")
args = parser.parse_args()
source = args.source
target = args.target

#function
def results(file_path):
    
    with open(file_path, 'r') as f:
        content = f.read()
        
        if 'SUCCESS' in content:
            print("Bezig met het verwerken van",file_path,)
            print("Resultaat in file",file_path,"is SUCCESS")
            return("success")
        
        elif 'FAILED' in content:
            print("Bezig met het verwerken van",file_path,)
            print("Resultaat in file",file_path,"is FAILED")
            return("failed")
        
        else:
            print("Bezig met het verwerken van",file_path,)
            print("Resultaat in file",file_path,"=> INCOMPLETE")
            return("incomplete")

#counters
counter_success = 0
counter_failed = 0
counter_incomplete = 0

#source directory
if os.path.exists(source):
    print("Source folder", source, "bestaat.")

else:
    print("Source folder", source, "bestaat niet.")
    exit(100)

#target directory
if os.path.exists(target):
    print("Target folder", target, "bestaat.")

else:
    os.mkdir(target)
    print("Target folder", target, "aangemaakt.")

#change to directory
os.chdir(source)

#read logfiles
for file in os.listdir():
    if file.endswith(".log"):
        file_path = f"{source}\{file}"
        result = results(file_path)
        
        if result == "success":
            counter_success += 1
        
        if result == "failed":
            counter_failed += 1
        
        if result == "incomplete":
            counter_incomplete += 1

#change directory
os.chdir(target)

#create date var
today = str(datetime.datetime.today().strftime('%d/%m/%Y'))

#create output file
file = open('Backup_report.txt','w')
file.write('########### ' + today + ' ########### \n')
file.write('Input directory: C:\BackupLogs\In \n')
file.write('Aantal gelukte backups:\t\t' + str(counter_success) + '\n')
file.write('Aantal gefaalde backups:\t' + str(counter_failed) + '\n')
file.write('Aantal incomplete backups:\t' + str(counter_incomplete) + '\n')
file.write('##################################')
file.close()
print("De datum van vandaag is",today)
print("Aanmaken van de rapport file " + target + "\Backup_report.txt.")
print("Rapport file aangemaakt")