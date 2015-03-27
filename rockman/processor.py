from rockman import settings


def default(request):
    return {
        'css_file': ['base/css/bootstrap/bootstrap.min.css',
                     'base/css/base.css',
                     ],
        'js_file': ['base/js/bootstrap/bootstrap.min.js',
                    'base/js/base.js',
                    # 'base/js/tabs.js',
                    ],
        'js_file_url': ['https://ajax.googleapis.com/ajax/libs/angularjs/1.2.8/angular.min.js',
                        'https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js',
                    ],
        'page_title': 'Kyle & Emily',
        'window_title': 'Kyle Rockman and Emily Buschang',  #use full names for search engine optimization
        'footer_text': 'Kyle and Emily built this website together from scratch.',
        'footer_email': 'buschang.rockman.wedding@gmail.com',
    }