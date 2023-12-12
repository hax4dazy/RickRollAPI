from flask import Flask, redirect, Response
from peewee import *
from dbClasses import *

app = Flask(__name__)

db.create_tables([stats, isTheDatabaseSetup])

if isTheDatabaseSetup.get_or_create() is not True:
    isTheDatabaseSetup.insert(isSetup=True).execute()
    stats.insert(name='rickRollCount', count=0).execute()
    print(f'First run detected. Have fun rickrolling the world!')


@app.route('/', methods=['GET'])
def rickroll():
    try:
        rickRollCount = stats.get_or_none(stats.name == 'rickRollCount').count
        rickRollCount += 1
        stats.update(count=rickRollCount).where(stats.name == 'rickRollCount').execute()
    except Exception as e:
        return Response(f'Error: {e}', status=500)
    print(rickRollCount)
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", code=302)
    

@app.route('/stats', methods=['GET'])
def count():
    try:
        rickRollCount = stats.get_or_none(stats.name == 'rickRollCount').count
    except Exception as e:
        return Response(f'Error: {e}', status=500)
    return Response(f'Amount of people who have gotten rickrolled: {rickRollCount}', status=200)

if __name__ == '__main__':
    app.run()