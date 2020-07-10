from flask import Blueprint, jsonify, request
from utils import Deck
endpoints_blueprint = Blueprint('endpoints_blueprint', __name__)

deck_obj = Deck()


@endpoints_blueprint.route('/board_setup')
def board_setup():
    global deck_obj
    return jsonify(deck_obj.setup_board())


@endpoints_blueprint.route('/deal_cards')
def deal_cards():
    global deck_obj
    if not deck_obj.game_deck:
        return(
            {
                "msg": "ERROR: Board has not yet been setup"
            }
        )
    player_id = request.args.get('player_id')
    return jsonify(deck_obj.deal_cards(player_id=player_id))


@endpoints_blueprint.route('/player_cards')
def player_cards():
    global deck_obj
    return jsonify(deck_obj.get_player_cards())
