from datetime import datetime
import shutil, os

folders = "C:\\Code;C:\\Joobie"
destFolder = "\\\\beans\\md0\\KuiperBackups"
logfile = open("C:\\Code\\Auto Maytor\\logs\\log" + datetime.now().strftime("%m%d%Y") +  ".txt", "a")

def writeToDebug(log):
    logfile.write(datetime.now().strftime("%m/%d/%Y %H:%M:%S") + " --- " + log + "\n")

def main():
    try:
        writeToDebug("Spinning up: " + datetime.now().strftime("%H:%M:%S") + "...")
        writeToDebug("Removing backups older than 30 days...")
        writeToDebug("--- --- --- --- --- --- --- --- --- --- --- --- --- --- ---")
        count = 0
        for directory in os.listdir(destFolder):
            try:
                mtime = os.path.getmtime(destFolder + "\\" + directory)
                mtime = format(datetime.fromtimestamp(mtime).strftime("%d/%m/%y"))
                d1 = datetime.strptime(mtime, "%d/%m/%y")
                d2 = datetime.now().strftime("%d/%m/%y")
                d2 = datetime.strptime(d2, "%d/%m/%y")
                if abs((d1 - d2).days) > 30:
                    shutil.rmtree(destFolder + "\\" + directory)
                    count += 1
            except Exception as e:
                writeToDebug("Error occurred when removing old backups: " + str(e))

        if count > 0:
            writeToDebug(count + " backups(s) removed...")
        else:
            writeToDebug("No backups to remove...")

        writeToDebug("--- --- --- --- --- --- --- --- --- --- --- --- --- --- ---")
        writeToDebug("Backing up folders " + folders + " from Kuiper to Beans...")
        writeToDebug("Changing directory to C:\\...")
        os.chdir("C:\\")
        for path in folders.split(";"):
            writeToDebug("Backing up " + path + "...")
            shutil.copytree(path, "\\\\beans\\md0\\KuiperBackups\\Backup" + datetime.now().strftime("%m%d%Y") + "\\" + os.path.basename(path))
            writeToDebug("Done copying " + path + "...")
        
        writeToDebug("Done.")
    except Exception as e:
        writeToDebug("Error: " + str(e))
    finally:
        logfile.close()

main()