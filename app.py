from flask import Flask, render_template, url_for
import datetime

app = Flask(__name__)

# 24 Romantic Ideas for the Advent Calendar
calendar_content = [
    "Vítej Bubínečku ve svém novém adventním kalendáři. Vánoce už se nám kvapem blíží a já bych Ti rád zkrátil čekání.\n\nKaždý den Tě čeká nové překvapení, díky kterému se snad budeš víc a víc těšit na ten náš velký Vánoční den. Teprve se rozjíždíme, a tak je Tvoje první překvapení poměrně jednoduché. Večer, až naše Vajanka usne, tak si pustíme první letošní Vánoční film dle Tvé volby a čeká Tě u něj krásná masáž a pohoštění. Hurá, těšíš se?\n\nNezapomeň si zítra otevřít další okýnko! Miluju Tě <3",
    "Virtual Hug: A small animation or message to remind her you’re thinking of her.",
    "Winter Song: Share a romantic Christmas song link.",
    "Gift Voucher: A handmade voucher for something she'd enjoy.",
    "Quote of the Day: Romantic or holiday-inspired quote.",
    "Tak tu máme den šest a s ním páteček. Myslím, že nastal čas na další filmový večer s masáží a pohoštěním. Tak jaký film vybereš tentokrát?",
    "Mini Story: A short, sweet story about her.",
    "Vítej v osmém dni Bubínečíku. Dnes Tě čeká krásná večerní procházka zakončená svařákem a následně horká vana na rozmrznutí.",
    "Christmas Recipe: A favorite holiday recipe you could make together.",
    "Compliment List: A list of compliments for her.",
    "Puzzle: Create a mini puzzle or riddle with a surprise message.",
    "Tak tu máme den 12 a s ním myslím nastal čas na další předváčnoční masáž u Vánočního filmu. Tak na co koukáme dnes?",
    "Video Message: A recorded message from you.",
    "Share a Secret: Something she doesn’t know yet.",
    "Poem: A short, romantic poem you wrote.",
    "Vítám Tě v dalším dnu. Doufám, že Tě kalendář zatím baví a líbí se Ti. Taky ale vím, že nejvíc ze všeho oceňuješ masáže. Takže... další masáž a film? Není To ohrané?"
]

@app.route('/')
def home():
    today = datetime.datetime.now()
    day = today.day
    all_open = False

    return render_template('calendar.html', content=calendar_content, today=day, all_open=all_open)

@app.route('/day/2')
def day_2():
    message = """
    <h2> Jako další pro Tebe mám jednu z mých oblíbených Vánočních vzpomínek. Pamatuješ? </h2>
    """
    return render_template('day.html', day=2, message=message, image_url=url_for('static', filename='images/christmas-memory.jpeg'))

@app.route('/day/3')
def day_3():
    message = """
    <h2> Jako další bych Ti rád vyjmenoval důvody, proč s Tebou miluji Vánoce: </h2>
    <ol>
        <li>O Vánocích s Tebou cítím opravdovou Vánoční pohodu jako s nikým jiným.</li>
        <li>Miluju naše vlastní tradice jako je pouštění lodiček.</li>
        <li>Miluju, že máme rádi stejné Vánoční filmy.</li>
        <li>Miluju to, jak se s Tebou o Vánocích cítím.</li>
    </ol>
    """
    return render_template('day.html', day=3, message=message)

@app.route("/day/4")
def day_4():
    message = """
    <h2>🎄 **Recept na Svařák** 🍷</h2>
    <p>Ahoj Bubínku! Na dnešní den pro Tebe mám jeden z mých oblíbených receptů na zimní večery – Svařák! 🍷✨ Tento hřejivý nápoj je ideální na procházky po sněhu nebo na večerní relax u TV. Tak pojďme na to!</p>

    <h3>**Ingredience:**</h3>
    <ul>
        <li>1 láhev červeného vína 🍇</li>
        <li>2 lžíce cukru 🍬</li>
        <li>1 pomeranč 🍊</li>
        <li>3 hřebíčky 🌿</li>
        <li>2-3 kousky skořice 🌰</li>
        <li>2 hřebíčky kardamomu (pokud máš) 🧡</li>
        <li>1-2 lžíce rumu 🍹 (nebo víc, pokud máš rád/a 😉)</li>
    </ul>

    <h3>**Postup:**</h3>
    <ol>
        <li>Nejprve si nalij víno do hrnce a zahřej ho. Nevař, jen zahřívej! 🔥</li>
        <li>Pomeranč nakrájej na kolečka a přidej je do vína. 🍊</li>
        <li>Přidej cukr, skořici, hřebíčky a kardamom. Míchej, dokud se cukr nerozpustí. 🍬</li>
        <li>Nech svařák prohřát a občas zamíchej. Při ohřívání si užívej vůni, která se začne šířit po celém pokoji! 🌲</li>
        <li>Jakmile je nápoj hezky horký, přidej trochu rumu podle chuti. 🍹</li>
        <li>Před podáváním sceď, aby se odstranily koření a ovoce. Poté si užij hřejivý Svařák v oblíbeném hrníčku. ☕</li>
        <li>Pokud chceš, přidej ještě kousek pomerančové kůry na ozdobu. 🍊🎉</li>
    </ol>

    <p>Teď už stačí jen se pohodlně usadit a užívat si krásné Vánoční večery s Tvým oblíbeným nápojem! 🌟</p>
    <p><strong>P.S.</strong> A nezapomeň si zítra otevřít další okýnko! 🌟 Miluju Tě! ❤️</p>
    """
    return render_template("day.html", day=4, message=message)

@app.route('/day/5')
def day_5():
    photos = [
        'jan.jpeg', 'feb.jpeg', 'mar.jpeg', 'apr.jpeg',
        'may.jpeg', 'jun.jpeg', 'jul.jpeg', 'aug.jpeg',
        'sep.jpeg', 'oct.jpeg', 'nov.jpeg', 'dec.jpg'
    ]
    return render_template('day5.html', day=5, photos=photos)

@app.route('/day/7')
def day_7():
    return render_template('day7.html')

@app.route('/day/9')
def day_9():
    return render_template('day9.html')

@app.route('/day/10')
def day_10():
    return render_template('day10.html')

@app.route('/day/11')
def day_11():
    return render_template('day11.html')

@app.route('/day/13')
def day_13():
    return render_template('day13.html')

@app.route('/day/14')
def day_14():
    return render_template('day14.html')

@app.route('/day/15')
def day_15():
    return render_template('day15.html')

@app.route('/day/17')
def day_17():
    return render_template('day17.html')

@app.route('/day/18')
def day_18():
    return render_template('day18.html')

@app.route('/day/19')
def day_19():
    return render_template('day19.html')

@app.route('/day/20')
def day_20():
    return render_template('day20.html')

@app.route('/day/21')
def day_21():
    return render_template('day21.html')

@app.route('/day/22')
def day_22():
    return render_template('day22.html')

@app.route('/day/23')
def day_23():
    return render_template('day23.html')

@app.route('/day/24')
def day_24():
    return render_template('day24.html')

@app.route('/day/<int:day>')
def day_content(day):
    if day == 1:
        return render_template('day.html', content=calendar_content[0], day=1)
    elif 1 <= day <= len(calendar_content):
        return render_template('day.html', content=calendar_content[day-1], day=day)
    else:
        return "Day not found", 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
