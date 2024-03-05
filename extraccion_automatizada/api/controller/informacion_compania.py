from flask import Flask, jsonify, request, Blueprint
from ..commands.create_credit_card import CreateCreditCard
from ..commands.get_credit_card import GetCreditCards
from ..commands.health_credit_card import PingCommandCreditCard
from ..commands.reset_credit_card import ResetRouteDataBaseCreditCard
import os
from ..models.credit_card import CreditCardJsonSchema

credit_card_schema=CreditCardJsonSchema()
credit_card_blueprint = Blueprint('scores', __name__)


# 1. Recu
@credit_card_blueprint.route('/credit-cards', methods = ['POST'])
def create_credit_card():
    token_bearer=request.headers.get('Authorization')
    if token_bearer is None:
        token=""
    else:
       token=token_bearer

    json = request.get_json()
    fields_request=['cardNumber', 'cvv', 'expirationDate', 'cardHolderName']

    for field in fields_request:
        if field not in json:
            json[field]=""
    
    result = CreateCreditCard(json['cardNumber'], json['cvv'], json['expirationDate'],  ['cardHolderName'], token).execute()    
    return jsonify(result),201

