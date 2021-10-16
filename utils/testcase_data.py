from utils.openpyxlfunction import *
import pathlib
# Search Keyword
account = "xohef93592@activesniper.com"
password = "asdfghqwerty#123"

filename = "JOBLISTING.xlsx"
bdjobsheet = "BDJOB"
baytjobsheet = "Bayt"
dicejobsheet = "Dice"
upworkjobsheet = "Upwork"
monsterjobsheet= "Monster"
ConfigPage = "config"
filepath = pathlib.Path(__file__).parent / f"{filename}"
searchkeyword = readData(filepath, ConfigPage, 3, 2)
RequiredParameter = readData(filepath, ConfigPage, 4, 2)