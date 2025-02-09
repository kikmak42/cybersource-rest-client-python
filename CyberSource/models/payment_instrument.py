# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PaymentInstrument(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'links': 'TmsV1InstrumentIdentifiersPost200ResponseLinks',
        'id': 'str',
        'object': 'str',
        'state': 'str',
        'bank_account': 'TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBankAccount',
        'card': 'TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedCard',
        'buyer_information': 'TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation',
        'bill_to': 'TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBillTo',
        'processing_information': 'TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedProcessingInformation',
        'merchant_information': 'TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedMerchantInformation',
        'meta_data': 'TmsV1InstrumentIdentifiersPost200ResponseMetadata',
        'instrument_identifier': 'TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier'
    }

    attribute_map = {
        'links': '_links',
        'id': 'id',
        'object': 'object',
        'state': 'state',
        'bank_account': 'bankAccount',
        'card': 'card',
        'buyer_information': 'buyerInformation',
        'bill_to': 'billTo',
        'processing_information': 'processingInformation',
        'merchant_information': 'merchantInformation',
        'meta_data': 'metaData',
        'instrument_identifier': 'instrumentIdentifier'
    }

    def __init__(self, links=None, id=None, object=None, state=None, bank_account=None, card=None, buyer_information=None, bill_to=None, processing_information=None, merchant_information=None, meta_data=None, instrument_identifier=None):
        """
        PaymentInstrument - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._object = None
        self._state = None
        self._bank_account = None
        self._card = None
        self._buyer_information = None
        self._bill_to = None
        self._processing_information = None
        self._merchant_information = None
        self._meta_data = None
        self._instrument_identifier = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if object is not None:
          self.object = object
        if state is not None:
          self.state = state
        if bank_account is not None:
          self.bank_account = bank_account
        if card is not None:
          self.card = card
        if buyer_information is not None:
          self.buyer_information = buyer_information
        if bill_to is not None:
          self.bill_to = bill_to
        if processing_information is not None:
          self.processing_information = processing_information
        if merchant_information is not None:
          self.merchant_information = merchant_information
        if meta_data is not None:
          self.meta_data = meta_data
        if instrument_identifier is not None:
          self.instrument_identifier = instrument_identifier

    @property
    def links(self):
        """
        Gets the links of this PaymentInstrument.

        :return: The links of this PaymentInstrument.
        :rtype: TmsV1InstrumentIdentifiersPost200ResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this PaymentInstrument.

        :param links: The links of this PaymentInstrument.
        :type: TmsV1InstrumentIdentifiersPost200ResponseLinks
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this PaymentInstrument.
        Unique identification number assigned by CyberSource to the submitted request.

        :return: The id of this PaymentInstrument.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PaymentInstrument.
        Unique identification number assigned by CyberSource to the submitted request.

        :param id: The id of this PaymentInstrument.
        :type: str
        """

        self._id = id

    @property
    def object(self):
        """
        Gets the object of this PaymentInstrument.
        Describes type of token.

        :return: The object of this PaymentInstrument.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this PaymentInstrument.
        Describes type of token.

        :param object: The object of this PaymentInstrument.
        :type: str
        """
        allowed_values = ["paymentInstrument"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def state(self):
        """
        Gets the state of this PaymentInstrument.
        Current state of the token.

        :return: The state of this PaymentInstrument.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this PaymentInstrument.
        Current state of the token.

        :param state: The state of this PaymentInstrument.
        :type: str
        """
        allowed_values = ["ACTIVE", "CLOSED"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def bank_account(self):
        """
        Gets the bank_account of this PaymentInstrument.

        :return: The bank_account of this PaymentInstrument.
        :rtype: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBankAccount
        """
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        """
        Sets the bank_account of this PaymentInstrument.

        :param bank_account: The bank_account of this PaymentInstrument.
        :type: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBankAccount
        """

        self._bank_account = bank_account

    @property
    def card(self):
        """
        Gets the card of this PaymentInstrument.

        :return: The card of this PaymentInstrument.
        :rtype: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this PaymentInstrument.

        :param card: The card of this PaymentInstrument.
        :type: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedCard
        """

        self._card = card

    @property
    def buyer_information(self):
        """
        Gets the buyer_information of this PaymentInstrument.

        :return: The buyer_information of this PaymentInstrument.
        :rtype: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation
        """
        return self._buyer_information

    @buyer_information.setter
    def buyer_information(self, buyer_information):
        """
        Sets the buyer_information of this PaymentInstrument.

        :param buyer_information: The buyer_information of this PaymentInstrument.
        :type: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation
        """

        self._buyer_information = buyer_information

    @property
    def bill_to(self):
        """
        Gets the bill_to of this PaymentInstrument.

        :return: The bill_to of this PaymentInstrument.
        :rtype: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBillTo
        """
        return self._bill_to

    @bill_to.setter
    def bill_to(self, bill_to):
        """
        Sets the bill_to of this PaymentInstrument.

        :param bill_to: The bill_to of this PaymentInstrument.
        :type: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBillTo
        """

        self._bill_to = bill_to

    @property
    def processing_information(self):
        """
        Gets the processing_information of this PaymentInstrument.

        :return: The processing_information of this PaymentInstrument.
        :rtype: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this PaymentInstrument.

        :param processing_information: The processing_information of this PaymentInstrument.
        :type: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def merchant_information(self):
        """
        Gets the merchant_information of this PaymentInstrument.

        :return: The merchant_information of this PaymentInstrument.
        :rtype: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedMerchantInformation
        """
        return self._merchant_information

    @merchant_information.setter
    def merchant_information(self, merchant_information):
        """
        Sets the merchant_information of this PaymentInstrument.

        :param merchant_information: The merchant_information of this PaymentInstrument.
        :type: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedMerchantInformation
        """

        self._merchant_information = merchant_information

    @property
    def meta_data(self):
        """
        Gets the meta_data of this PaymentInstrument.

        :return: The meta_data of this PaymentInstrument.
        :rtype: TmsV1InstrumentIdentifiersPost200ResponseMetadata
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """
        Sets the meta_data of this PaymentInstrument.

        :param meta_data: The meta_data of this PaymentInstrument.
        :type: TmsV1InstrumentIdentifiersPost200ResponseMetadata
        """

        self._meta_data = meta_data

    @property
    def instrument_identifier(self):
        """
        Gets the instrument_identifier of this PaymentInstrument.

        :return: The instrument_identifier of this PaymentInstrument.
        :rtype: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier
        """
        return self._instrument_identifier

    @instrument_identifier.setter
    def instrument_identifier(self, instrument_identifier):
        """
        Sets the instrument_identifier of this PaymentInstrument.

        :param instrument_identifier: The instrument_identifier of this PaymentInstrument.
        :type: TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier
        """

        self._instrument_identifier = instrument_identifier

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PaymentInstrument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
