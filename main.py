# Main Python Script

from vars import *
import time
import os

rev = "cd .. && "

print({VIOLET}"================================================")
print({"             {HIGHLIGHT}{CYAN}|Starting Script|                  ")
print({VIOLET}"================================================"{END})
time.sleep(1)

print()
print("             {HIGHLIGHT}{CYAN}|CLONING TREES|{END}                    ")
print()
os.system(f"{rev}git clone {DT} {L_DT}")
os.system(f"{rev}git clone {VT} {L_VT}")
os.system(f"{rev}git clone {KT} {L_KT}")

print()
print("            {HIGHLIGHT}{CYAN}|CLONING INTERFACES|{END}                ")
print()
os.system(f"{rev}git clone {IMS} {L_IMS}")
os.system(f"{rev}git clone {INTERFACES} {L_INTERFACES}")

print()
print("              {HIGHLIGHT}{CYAN}|CLONING ADDONS|{END}                 ")
print()
os.system(f"{rev}git clone {RM_PARTS} {L_RM_PARTS}")
os.system(f"{rev}git clone {DIRAC} {L_DIRAC}")

print()
print("             {HIGHLIGHT}{CYAN}|APPLYING PATCHES|{END}                ")
print()
os.system(f"mv 0001-build-Add-option-to-append-vbmeta-image-to-boot-imag.patch /home/{OS}{DIR}/{BUILD_PATCH}/")
os.system(f"{rev}cd {BUILD_PATCH}/ && git apply -v 0001-build-Add-option-to-append-vbmeta-image-to-boot-imag.patch")
print()
print("                 {HIGHLIGHT}{GREEN}|Patch Applied Sucessfully|{END}                   ")
print()

os.system(f"mv 0001-Partially-Revert-Remove-references-to-deprecated-dev.patch /home/{OS}{DIR}/{FRAMEWORK_PATCH}/")
os.system(f"{rev}cd {FRAMEWORK_PATCH}/ && git apply -v 0001-Partially-Revert-Remove-references-to-deprecated-dev.patchh")
print()
print("                 {HIGHLIGHT}{GREEN}|Patch Applied Sucessfully|{END}                   ")
print()

print(f"{YELLOW}==========================================")
print(f"{HIGHLIGHT}{RED} THE SCRIPT EXECUTION FINISHED ")
print(f"{YELLOW}==========================================")



 



