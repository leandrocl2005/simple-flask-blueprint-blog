from flask import Blueprint, render_template

posts_db = [
    {
        'id': 1,
        'title': 'First Post',
        'body': "É preciso amar as pessoas como se não houvesse amanhã, porque se você parar para pensar, na verdade não há.",
        'created': '12/12/2018',
        'author_id': 1,
        'username': 'Ted' 
    },
    {
        'id': 2,
        'title': 'Second Post',
        'body': "Nunca deixe que lhe digam que não vale a pena acreditar no sonho que se tem ou que os seus planos nunca vão dar certo ou que você nunca vai ser alguém...",
        'created': '09/12/2017',
        'author_id': 1,
        'username': 'Ted' 
    },
    {
        'id': 3,
        'title': 'Third Post',
        'body': "Às vezes nem me preocupo tanto comigo... Mas há pessoas que amo e não quero vê-las sofrer.",
        'created': '12/10/2017',
        'author_id': 3,
        'username': 'Bia' 
    }
]

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    posts = posts_db # pegar do banco de dados
    return render_template('blog/index.html', posts=posts)