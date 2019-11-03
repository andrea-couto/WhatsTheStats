import dash
import flask
import os
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import queryTheModel

import instaloader
instagramLoader = instaloader.Instaloader()

app = dash.Dash(__name__)

app.layout = html.Div(
	children = [
	html.H1(
		children='What\'s the Stats?',
		style = {
		'textAlign': 'center', 
		'color': '#c94c4c',
		'fontFamily': 'helvetica',
		'fontSize': '5em'
		}
	),

	html.Div(
		children = '''
		A web application for analyzing user engagement with company products.
		''',
		style = {
		'textAlign': 'center', 
		'color': '#c94c4c',
		'fontFamily': 'helvetica',
		'fontSize': '2em',
		'paddingBottom': '2em'
		}
	),

	html.Label('Date (for gathering user data)', style = { 'display': 'block', 'fontWeight': 'bold' }),
	dcc.RadioItems(
		id = 'date',
        options = [
            {'label': 'Today', 'value': 'Today'},
            {'label': 'Tomorrow', 'value': 'Tomorrow'}
        ],
        value ='Today',
        style = {
        	'display': 'block',
        	'paddingBottom': '1em'
        }
    ),

    html.Label('Tag (i.e. #wayfair)', style = { 'display': 'block', 'fontWeight': 'bold'}),
    dcc.Input(
    	id = 'tag',
    	value ='#tag', 
    	type ='text', 
    	style = { 
    		'textAlign': 'center',
    	}
    ),


    html.Label('Product (company product for analysis)', style = { 'display': 'block', 'paddingTop': '1em', 'fontWeight': 'bold'}),
    dcc.Dropdown(
    	id = 'product',
        options = [
            {'label': 'Furniture', 'value': 'furniture'},
            {'label': 'Meatballs', 'value': 'meatballs'}
        ],
        value = 'meatballs',
        style = { 
	        'display': 'inline-block', 
	        'width': '50%'
        }
    ),

    html.Br(),
    html.Br(), 
    # TODO figure out how to pull in styling

    html.Button('Submit', id='button', style = { 'display': 'inline-block'}),

	# TODO this is just stand in will need to populate this once we connect it up
	dcc.Graph(
		id = 'test',
		figure = {
			'data': [
				{'x': ['Furniture','Meatballs','Other'], 'y': [34,23,76], 'type': 'bar', 'name': 'SF'},
			],
			'layout': {
				'title': 'Model Classifications based on >50% confidence'
			}
		},
		style = {
			'paddingTop': '2em',
			'display': 'none'
		}
	),

	html.Label('data is for demo purposes only (not actually derived)', style = { 'display': 'block', 'paddingTop': '1em', 'fontWeight': 'bold'}),
],
style = { 'textAlign': 'center'})

'''
some pseudocode for what to do next to hook this project up 

callback for pressing submit
	hashtag = get element by id 'tag'
	date = get element by id 'date'
	postfilter = "<date>"
	postfilter = "not is_video"
	instagramLoader.download_hashtag(hashtag, max_count=None, post_filter=postfilter, fast_update=False)

	once images are downloaded to #hashtag
	for photo in downloadedInstagramImagesFolder
		pass photo to model using queryTheModel.get_prediction(photoPath, projid, modelid)

'''

if __name__ == '__main__':
	app.run_server(debug=True)