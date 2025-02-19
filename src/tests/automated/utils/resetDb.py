from .db import getConnection

def resetDb():
    db = getConnection(True)
    cursor = db.cursor(buffered=True)
    try:
        runScript('../../../buildConfig/prod/create.sql', cursor)
        runScript('../../../buildConfig/dev/data.sql', cursor)
    finally:
        cursor.close()
        db.close()


def runScript(path, cursor):
    sql = ""
    with open(path, 'r') as f:
        sql = f.read()
    commands = splitScript(sql)
    for i in range(len(commands)):
        cursor.execute(commands[i])

def splitScript(text: str):
    delimiter = ';'
    command = ''
    commands = []

    for line in text.splitlines():
        line = line.strip()

        if line.lower().startswith('delimiter'):
            delimiter = line.split()[1]
            continue

        if not line.endswith(delimiter):
            if not line == "":
                command += f"{line}\n"
        else:
            command += f"{line.rstrip(delimiter)}"
            commands.append(command)
            command = ""
            delimiter = ";"
    return commands
