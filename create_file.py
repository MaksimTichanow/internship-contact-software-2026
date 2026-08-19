with open("names_dos.txt", "w", encoding="utf-8", newline="\r\n") as datei:
    datei.write("""

      Maksim
      Fabian
      Tanja
      Benjamin
      Waleri

      """)


with open("names_unix.txt", "w", encoding="utf-8", newline="\n") as datei:
    datei.write("""

      Maksim
      Fabian
      Tanja
      Benjamin
      Waleri

      """)