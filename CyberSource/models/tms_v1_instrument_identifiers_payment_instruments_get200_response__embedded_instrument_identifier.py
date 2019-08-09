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


class TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier(object):
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
        'object': 'str',
        'state': 'str',
        'id': 'str',
        'card': 'TmsV1InstrumentIdentifiersPost200ResponseCard',
        'bank_account': 'TmsV1InstrumentIdentifiersPost200ResponseBankAccount',
        'processing_information': 'TmsV1InstrumentIdentifiersPost200ResponseProcessingInformation',
        'metadata': 'TmsV1InstrumentIdentifiersPost200ResponseMetadata'
    }

    attribute_map = {
        'links': '_links',
        'object': 'object',
        'state': 'state',
        'id': 'id',
        'card': 'card',
        'bank_account': 'bankAccount',
        'processing_information': 'processingInformation',
        'metadata': 'metadata'
    }

    def __init__(self, links=None, object=None, state=None, id=None, card=None, bank_account=None, processing_information=None, metadata=None):
        """
        TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier - a model defined in Swagger
        """

        self._links = None
        self._object = None
        self._state = None
        self._id = None
        self._card = None
        self._bank_account = None
        self._processing_information = None
        self._metadata = None

        if links is not None:
          self.links = links
        if object is not None:
          self.object = object
        if state is not None:
          self.state = state
        if id is not None:
          self.id = id
        if card is not None:
          self.card = card
        if bank_account is not None:
          self.bank_account = bank_account
        if processing_information is not None:
          self.processing_information = processing_information
        if metadata is not None:
          self.metadata = metadata

    @property
    def links(self):
        """
        Gets the links of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.

        :return: The links of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        :rtype: TmsV1InstrumentIdentifiersPost200ResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.

        :param links: The links of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        :type: TmsV1InstrumentIdentifiersPost200ResponseLinks
        """

        self._links = links

    @property
    def object(self):
        """
        Gets the object of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        'Describes type of token.'  Valid values: - instrumentIdentifier 

        :return: The object of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        'Describes type of token.'  Valid values: - instrumentIdentifier 

        :param object: The object of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        :type: str
        """

        self._object = object

    @property
    def state(self):
        """
        Gets the state of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        'Current state of the token.'              Valid values: - ACTIVE - CLOSED 

        :return: The state of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        'Current state of the token.'              Valid values: - ACTIVE - CLOSED 

        :param state: The state of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        :type: str
        """

        self._state = state

    @property
    def id(self):
        """
        Gets the id of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        The ID of the existing instrument identifier to be linked to the newly created payment instrument.

        :return: The id of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        The ID of the existing instrument identifier to be linked to the newly created payment instrument.

        :param id: The id of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        :type: str
        """
        if id is not None and len(id) > 32:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `32`")
        if id is not None and len(id) < 16:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `16`")

        self._id = id

    @property
    def card(self):
        """
        Gets the card of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.

        :return: The card of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        :rtype: TmsV1InstrumentIdentifiersPost200ResponseCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.

        :param card: The card of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        :type: TmsV1InstrumentIdentifiersPost200ResponseCard
        """

        self._card = card

    @property
    def bank_account(self):
        """
        Gets the bank_account of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.

        :return: The bank_account of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        :rtype: TmsV1InstrumentIdentifiersPost200ResponseBankAccount
        """
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        """
        Sets the bank_account of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.

        :param bank_account: The bank_account of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        :type: TmsV1InstrumentIdentifiersPost200ResponseBankAccount
        """

        self._bank_account = bank_account

    @property
    def processing_information(self):
        """
        Gets the processing_information of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.

        :return: The processing_information of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        :rtype: TmsV1InstrumentIdentifiersPost200ResponseProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.

        :param processing_information: The processing_information of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        :type: TmsV1InstrumentIdentifiersPost200ResponseProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def metadata(self):
        """
        Gets the metadata of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.

        :return: The metadata of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        :rtype: TmsV1InstrumentIdentifiersPost200ResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.

        :param metadata: The metadata of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier.
        :type: TmsV1InstrumentIdentifiersPost200ResponseMetadata
        """

        self._metadata = metadata

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
        if not isinstance(other, TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedInstrumentIdentifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
