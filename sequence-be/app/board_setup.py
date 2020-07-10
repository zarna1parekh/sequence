from flask import Blueprint, jsonify, request
from utils import Deck
board_setup_blueprint = Blueprint('board_setup_blueprint', __name__)

deck_obj = Deck()


@board_setup_blueprint.route('/board_setup')
def index_anyname():
    global deck_obj
    return jsonify(deck_obj.setup_board())


@board_setup_blueprint.route('/deal_cards')
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


@board_setup_blueprint.route('/player_cards')
def player_cards():
    global deck_obj
    return jsonify(deck_obj.get_player_cards())
