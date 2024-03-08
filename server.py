from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from flask import render_template, redirect, url_for
app = Flask(__name__)


data = [
{
"id": "1",
"title": "tabetomo",
"image": "https://cdn.vox-cdn.com/thumbor/9mq31P1NoK5nWS3iXNAj6UqXFfA=/0x0:3000x2000/1200x800/filters:focal(1260x760:1740x1240)/cdn.vox-cdn.com/uploads/chorus_image/image/63017335/L_Palmberg_TabeTomo_075.0.jpg",
"webpage": "https://www.tabetomonyc.com/",
"price": "$",
"summary": "named after its founder chef tomo, tabetomo (pronounced ‘ta-beh-to-mo’) translates directly from japanese to “eating buddy.” the restaurant serves a signature tonkotsu pork broth that prepared over 60 hours and specializes in jiro-style. located in the heart of manhattan’s east village, on the busy cross streets of st. marks and avenue a, tabetomo caters to an eclectic crowd, ranging from native connoisseurs of noodles to the first-time customer of tsukemen.",
"popular": ["Jiro style Ramen", "Tsukement"],
"types": ["Noodles"],
"reviews": [
            {"username": "Kento Yanagishita", "rate": "⭐️⭐️⭐️⭐️⭐️",  "review": "Absolutely love Tabetomo! The Jiro-style ramen is a game-changer, and the tsukemen is a must-try. The rich tonkotsu broth is worth the 60-hour preparation. Cozy spot in the East Village with an authentic Japanese vibe."},
            # Add more reviews as needed
        ],
"area": "East Village",
},
{
"id": "2",
"title": "E.A.K. Ramen",
"image": "https://pyxis.nymag.com/v1/imgs/5e7/d5c/28afc72eaa4c1beee50eb7d079b2ebf0a5-e-a-kramen-01.2x.rsocial.w600.jpg",
"webpage": "https://eakramen.com",
"price": "$",
"summary": "E.A.K. Ramen aka Machida Shoten in Japan, started back in 2008 in Machida City, Japan. This was our first shop to fulfill our goal to spread the IEKEI style of ramen to the world.",
"popular": ["Tsukemen", "Miso Ramen"],
"types": ["Noodles"],
"reviews": [
            {"username": "Emiri Yanagishita", "rate": "⭐️⭐️⭐️⭐️",  "review": "E.A.K. Ramen is a hidden gem! The IEKEI style is fantastic, and their tsukemen and miso ramen are my go-to choices. The flavors are authentic, and it feels like a taste of Japan right here in the city."},
            # Add more reviews as needed
        ],
"area": "Hell's Kitchen",
},
{
"id": "3",
"title": "Gyu-Kaku Japanese BBQ",
"image": "https://houstonsgotspice.com/wp-content/uploads/2020/03/IMG_0839-scaled.jpg",
"price": "$$",
"summary": "Spending time with Friends and Family is what Gyu-Kaku is all about. Gyu-Kaku offers the fun of Shared Plates",
"popular": ["Pork belly", "Kimchi"],
"types": ["BBQ", "Grill", "Meat"],
"reviews": [
        {"username": "Ed Sheeran", "rate": "⭐️⭐️⭐️⭐️",  "review": "Gyu-Kaku is my go-to place for Japanese BBQ. The shared plates make it perfect for group gatherings. The pork belly and kimchi are flavorful, and the grilling experience is always fun."},
        # Add more reviews as needed
    ],
"area": "Midtown",
},
{
"id": "4",
"title": "Tomi Jazz",
"image":"https://static01.nyt.com/images/2018/03/25/nyregion/25JOINT1/25JOINT1-videoSixteenByNineJumbo1600.jpg",
"webpage": "https://www.tomijazz.com",
"price": "$$",
"summary": "Small jazz club with great atmosphere! Get there early to wait in line so you can have a good view of the splendid jazz trio. Great crafted cocktails and tasty food. Cordial service and a fantastic atmosphere.",
"popular": ["Okonomiyaki", "Omrice"],
"types": ["Bar", "Grill", "Meat"],
"reviews": [
        {"username": "Harvey Spector", "rate": "⭐️⭐️⭐️⭐️⭐️", "review": "Tomi Jazz is a fantastic hidden oasis! The jazz trio sets a great atmosphere, and the crafted cocktails are top-notch. The okonomiyaki and omurice are a delight for the taste buds."},
        # Add more reviews as needed
    ],
"area": "Midtown",
},
{
"id": "5",
"title": "Kouzan",
"image": "https://d1ralsognjng37.cloudfront.net/0ccc7f7f-a21c-4b06-a2a6-6e7be9bef7e3",
"webpage": "https://www.kouzanny.com",
"price": "$$",
"summary": "Kouzan Japanese Restaurant, located on the Upper West Side, is a Japanese restaurant that prides itself on qulity food and service. Opened in 2007, Kouzan offers both traditional and inventive Japanese cuisine in an inviting and warm atmosphere. We welcome you to stop by for lunch and dinner.",
"popular": ["Sashimi", "Tuna roll"],
"types": ["Sushi", "seafood"],
"reviews": [
        {"username": "Balak Obama", "rate": "⭐️⭐️⭐️⭐️", "review": "Kouzan is my favorite spot for quality Japanese cuisine. The sashimi is fresh, and the tuna roll is a personal favorite. The warm atmosphere and welcoming service make it a perfect place for a delightful lunch or dinner."},
        # Add more reviews as needed
    ],
"area": "Upper West Side",
},
{
"id": "6",
"title": "Mei Jin Ramen",
"image": "https://media-cdn.tripadvisor.com/media/photo-s/1a/fd/52/f6/chili-beef-beef-broth.jpg",
"webpage": "https://www.meijinramen.com",
"price": "$",
"summary": "Since 2014, Meijin Ramen in New York City has been serving traditional Japanese ramen dishes, with the signature Tonkotsu broth and miso beef broth an absolute must for first-time visitors.",
"popular": ["Tonkotsu Ramen", "Miso Ramen"],
"types": ["Bar", "Grill", "Meat"],
"reviews": [
        {"username": "Taylor Swift", "rate": "⭐️⭐️⭐️", "review": "Mei Jin Ramen nails it with their traditional ramen dishes. The tonkotsu and miso ramen are flavorful, and the broth is on point. A go-to spot for ramen lovers in the city."},
        # Add more reviews as needed
    ],
"area": "Upper East Side",
},
{
"id": "7",
"title": "Nobu",
"image": "https://resizer.otstatic.com/v2/photos/wide-huge/1/50163957.jpg",
"webpage": "https://noburestaurants.com/fifty-seven/home",
"price": "$$",
"summary": "Nobu Matsuhisa is a globally-renowned chef, most well-known for his unique take on traditional Japanese cuisine with Peruvian ingredients, a style often referred to as Nobu Style. His vision can be understood through several keys:",
"popular": ["Shrimp Tempura", "Creamy Spicy Crab"],
"types": ["Bar", "seafood"],
"reviews": [
        {"username": "Kento Yanagishita", "rate": "⭐️⭐️⭐️⭐️", "review": "Nobu is a culinary masterpiece! The blend of Japanese and Peruvian ingredients creates unique flavors. The shrimp tempura and creamy spicy crab are heavenly. A high-end dining experience worth every penny."},
        # Add more reviews as needed
    ],
"area": "Midtwon",
},
{
"id": "8",
"title": "Katsu Hama",
"image": "https://i.redd.it/qocjoabmsao71.jpg",
"webpage": "https://katsu-hama.club",
"price": "$",
"summary": "Nestled in the heart of a bustling metropolis, a culinary haven is unveiled, where discerning palates are enthralled, and gastronomic memories are etched. This restaurant, founded with passion and dedication, stands as a testament to culinary artistry, where every dish is meticulously crafted to perfection. Since opening its doors several years ago, this establishment has been frequented by patrons seeking an unparalleled dining experience. ",
"popular": ["Ton Katsu", "Katsu Don"],
"types": ["Meat"],
"reviews": [
        {"username": "Ryosuke Tanaka", "rate": "⭐️⭐️⭐️⭐️⭐️", "review": "Katsu Hama is a true gem. The tonkatsu and katsu don are perfection. The attention to detail in crafting each dish is evident. A must-visit for anyone seeking an authentic Japanese dining experience."},
        # Add more reviews as needed
    ],
"area": "Midtown",
},
{
"id": "9",
"title": "Go! Go! Curry!",
"image": "https://b2257154.smushcdn.com/2257154/wp-content/themes/gogocurry/images/home2.jpg?lossy=1&strip=1&webp=1",
"webpage": "https://gogocurryamerica.com",
"price": "$",
"summary": "Visit us for authentic Japanese Comfort food without flying to Japan. We have over 70 locations in Japan and proudly serve the same authentic Japanese Katsu curry in the United States.",
"popular": ["Katsu Curry"],
"types": ["Curry"],
"reviews": [
        {"username": "Harry Potter", "rate": "⭐️⭐️⭐️⭐️", "review": "Go! Go! Curry! brings the taste of Japan to the U.S. The katsu curry is comforting and delicious. A convenient spot for those craving Japanese comfort food. Love the authentic flavors!"},
        # Add more reviews as needed
    ],
"area": "Greenwich Village",
},
{
"id": "10",
"title": "Masa",
"image": "https://pyxis.nymag.com/v1/imgs/145/86f/1a81b4362bead93bb9639d0383d1370e10-masa-01.2x.rsocial.w600.jpg",
"webpage": "https://www.masanyc.com",
"price": "$$$",
"summary": "Masayoshi Takayama's appreciation for food started at a young age, growing up working for his family’s fish market in a town of Tochigi Prefecture, Japan.",
"popular": ["Omakase"],
"types": ["bar", "sushi", "seafood"],
"reviews": [
        {"username": "Shrek Smith", "rate": "⭐️⭐️⭐️⭐️⭐️", "review": "Masa is a culinary journey! The omakase experience is unparalleled. Chef Takayama's attention to detail shines through every dish. A luxurious dining destination for those who appreciate the finest Japanese cuisine."},
        # Add more reviews as needed
    ],
"area": "Hell's Kitchen",
},
]



# ROUTES

@app.route('/')
def hello_world():
    kentoPick = ["1", "4", "10"]
    three_data = [element for element in data if element['id'] in kentoPick]
    return render_template('homepage.html', three_data=three_data)    

@app.route('/search/', defaults={'search_term': ''}, methods=['POST', 'GET'])
@app.route('/search/<search_term>', methods=['POST', 'GET'])
def searchMe(search_term):
    if request.method == 'POST':
        # Handle the POST request data
        search_term = request.form.get('search')

    if search_term:
        # Case-insensitive search by title
        results = [element for element in data if ((search_term.lower() in element.get('title', '').lower())
        or any(search_term.lower() in types.lower() for types in element.get('types', [])) 
        or any(search_term.lower() in popular.lower() for popular in element.get('popular', [])))]
        return render_template('search.html', data=results, search_term=search_term)
    else:
        # Handle the case when search_term is not provided (default behavior)
        return render_template('search.html', data=[], search_term=search_term)

     

@app.route('/view/<item_id>')
def view_item(item_id):
    oneData = next(element for element in data if element['id'] == str(item_id))
    return render_template('view.html', oneData=oneData)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Get form data
        item_id = str(len(data) + 1)
        item_title = request.form.get('title')
        item_image = request.form.get('image')
        item_webpage = request.form.get('webpage')
        item_price = request.form.get('price')
        item_summary = request.form.get('summary')
        item_popular = [str(element.strip()) for element in request.form.get('popular', '').split(',') if element.strip()]
        item_types = [str(element.strip()) for element in request.form.get('types', '').split(',') if element.strip()]
        item_reviews = [
            {
                'username': request.form.get('username'),
                'rate': request.form.get('rate'),
                'review': request.form.get('review')
            }
        ]
        item_area = request.form.get('area')

        # Validate form data (you may need more validation depending on your requirements)
        if not item_title or not item_area:
            return jsonify({'error': 'Title and Area are required'})

        # Save the data (replace this with your actual data storage mechanism)
        new_item = {
            'id': item_id,
            'title': item_title,
            'image': item_image,
            'webpage': item_webpage,
            'price': item_price,
            'summary': item_summary,
            'popular': item_popular,
            'types': item_types,
            'reviews': item_reviews,
            'area': item_area,
        }
        data.append(new_item)

        # Return success response
        return jsonify({'success': 'Item successfully created','item_id': item_id})

    # Render the template for adding a new item
    return render_template('add.html')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_item(id):
    # Retrieve item details based on id (replace this with your data retrieval mechanism)
    item = get_item_by_id(id)

    if request.method == 'POST':
        # Handle form submission and update the data (replace this with your data update mechanism)
        update_item(id, request.form)
        return jsonify({'success': 'Item successfully created','item_id': id})

    return render_template('edit.html', item=item)


def get_item_by_id(item_id):
    # Replace this with your data retrieval mechanism
    return next((item for item in data if item['id'] == item_id), None)

def update_item(item_id, form_data):
    # Subtract 1 if item IDs start from 1
    index = int(item_id) - 1

    item_title = form_data.get('title')
    item_image = form_data.get('image')
    item_webpage = form_data.get('webpage')
    item_price = form_data.get('price')
    item_summary = form_data.get('summary')
    item_popular = [str(element.strip()) for element in form_data.get('popular', '').split(',') if element.strip()]
    item_types = [str(element.strip()) for element in form_data.get('types', '').split(',') if element.strip()]
    item_reviews = [
        {
            'username': form_data.get('username'),
            'rate': form_data.get('rate'),
            'review': form_data.get('review')
        }
    ]
    item_area = form_data.get('area')

    # Save the updated data (replace this with your actual data storage mechanism)
    new_item = {
        'id': item_id,
        'title': item_title,
        'image': item_image,
        'webpage': item_webpage,
        'price': item_price,
        'summary': item_summary,
        'popular': item_popular,
        'types': item_types,
        'reviews': item_reviews,
        'area': item_area,
    }
    data[index] = new_item
    return jsonify({'success': 'Item successfully edited','item_id': item_id})
        


# AJAX FUNCTIONS



if __name__ == '__main__':
   app.run(debug = True)


