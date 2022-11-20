import sys
import subprocess
from unicodedata import normalize

# For use with pt_PT dictionary. Useless if using pt_BR
exceptions = {
    "cao": "cão",
    "mao": "mão",
    "pao": "pão",
    "sao": "são",
    "tao": "tão"
}

def hunspell(word):
    cmd = ("hunspell", "-d", "pt_BR")
    ps = subprocess.Popen(("echo", word), stdout=subprocess.PIPE)
    output = subprocess.check_output(cmd, stdin=ps.stdout)
    return(output.decode("utf-8").split('\n')[1])

def check_spell(word):
    if word in exceptions:
        return exceptions[word]

    hun = hunspell(str(word))
    if hun[0] == "*": # Word is in dictionary
        return word
    elif hun[0] == "+": # Word is derivated of an existing word in dictionary
        return word
    elif hun[0] == "&": # Word can be a mispelling word
        suggestions = hun.split(": ")[1].split(", ") # Hunspell suggested corrections
        for s in suggestions:
            if word == normalize("NFKD", s).encode("ascii", "ignore").decode("utf-8").lower():
                return s
    return False

if __name__=="__main__":
    check = check_spell(sys.argv[1])
    print(check)
