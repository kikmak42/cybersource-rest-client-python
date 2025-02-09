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


class RiskV1AuthenticationsPost201Response(object):
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
        'links': 'PtsV2PaymentsReversalsPost201ResponseLinks',
        'id': 'str',
        'submit_time_utc': 'str',
        'submit_time_local': 'str',
        'status': 'str',
        'reason': 'str',
        'message': 'str',
        'client_reference_information': 'Ptsv2payoutsClientReferenceInformation',
        'order_information': 'RiskV1AuthenticationsPost201ResponseOrderInformation',
        'consumer_authentication_information': 'RiskV1AuthenticationsPost201ResponseConsumerAuthenticationInformation',
        'error_information': 'PtsV2PaymentsPost201ResponseErrorInformation'
    }

    attribute_map = {
        'links': '_links',
        'id': 'id',
        'submit_time_utc': 'submitTimeUtc',
        'submit_time_local': 'submitTimeLocal',
        'status': 'status',
        'reason': 'reason',
        'message': 'message',
        'client_reference_information': 'clientReferenceInformation',
        'order_information': 'orderInformation',
        'consumer_authentication_information': 'consumerAuthenticationInformation',
        'error_information': 'errorInformation'
    }

    def __init__(self, links=None, id=None, submit_time_utc=None, submit_time_local=None, status=None, reason=None, message=None, client_reference_information=None, order_information=None, consumer_authentication_information=None, error_information=None):
        """
        RiskV1AuthenticationsPost201Response - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._submit_time_utc = None
        self._submit_time_local = None
        self._status = None
        self._reason = None
        self._message = None
        self._client_reference_information = None
        self._order_information = None
        self._consumer_authentication_information = None
        self._error_information = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if submit_time_local is not None:
          self.submit_time_local = submit_time_local
        if status is not None:
          self.status = status
        if reason is not None:
          self.reason = reason
        if message is not None:
          self.message = message
        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if order_information is not None:
          self.order_information = order_information
        if consumer_authentication_information is not None:
          self.consumer_authentication_information = consumer_authentication_information
        if error_information is not None:
          self.error_information = error_information

    @property
    def links(self):
        """
        Gets the links of this RiskV1AuthenticationsPost201Response.

        :return: The links of this RiskV1AuthenticationsPost201Response.
        :rtype: PtsV2PaymentsReversalsPost201ResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this RiskV1AuthenticationsPost201Response.

        :param links: The links of this RiskV1AuthenticationsPost201Response.
        :type: PtsV2PaymentsReversalsPost201ResponseLinks
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this RiskV1AuthenticationsPost201Response.
        An unique identification number assigned by CyberSource to identify the submitted request. It is also appended to the endpoint of the resource.

        :return: The id of this RiskV1AuthenticationsPost201Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RiskV1AuthenticationsPost201Response.
        An unique identification number assigned by CyberSource to identify the submitted request. It is also appended to the endpoint of the resource.

        :param id: The id of this RiskV1AuthenticationsPost201Response.
        :type: str
        """
        if id is not None and len(id) > 26:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `26`")

        self._id = id

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this RiskV1AuthenticationsPost201Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` Example `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC. 

        :return: The submit_time_utc of this RiskV1AuthenticationsPost201Response.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this RiskV1AuthenticationsPost201Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` Example `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC. 

        :param submit_time_utc: The submit_time_utc of this RiskV1AuthenticationsPost201Response.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

    @property
    def submit_time_local(self):
        """
        Gets the submit_time_local of this RiskV1AuthenticationsPost201Response.
        Time that the transaction was submitted in local time.

        :return: The submit_time_local of this RiskV1AuthenticationsPost201Response.
        :rtype: str
        """
        return self._submit_time_local

    @submit_time_local.setter
    def submit_time_local(self, submit_time_local):
        """
        Sets the submit_time_local of this RiskV1AuthenticationsPost201Response.
        Time that the transaction was submitted in local time.

        :param submit_time_local: The submit_time_local of this RiskV1AuthenticationsPost201Response.
        :type: str
        """

        self._submit_time_local = submit_time_local

    @property
    def status(self):
        """
        Gets the status of this RiskV1AuthenticationsPost201Response.
        The status for payerAuthentication 201 enroll and validate calls. Possible values are: - AUTHENTICATION_SUCCESSFUL - PENDING_AUTHENTICATION 

        :return: The status of this RiskV1AuthenticationsPost201Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this RiskV1AuthenticationsPost201Response.
        The status for payerAuthentication 201 enroll and validate calls. Possible values are: - AUTHENTICATION_SUCCESSFUL - PENDING_AUTHENTICATION 

        :param status: The status of this RiskV1AuthenticationsPost201Response.
        :type: str
        """

        self._status = status

    @property
    def reason(self):
        """
        Gets the reason of this RiskV1AuthenticationsPost201Response.
        The reason of the status. Possible values are: - Authentication_Completed_Or_Skipped_Sucessfully - Pending_Authentication 

        :return: The reason of this RiskV1AuthenticationsPost201Response.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this RiskV1AuthenticationsPost201Response.
        The reason of the status. Possible values are: - Authentication_Completed_Or_Skipped_Sucessfully - Pending_Authentication 

        :param reason: The reason of this RiskV1AuthenticationsPost201Response.
        :type: str
        """

        self._reason = reason

    @property
    def message(self):
        """
        Gets the message of this RiskV1AuthenticationsPost201Response.
        The message describing the reason of the status. Value is: - The cardholder is enrolled in Payer Authentication. Please authenticate the cardholder before continuing with the transaction. 

        :return: The message of this RiskV1AuthenticationsPost201Response.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this RiskV1AuthenticationsPost201Response.
        The message describing the reason of the status. Value is: - The cardholder is enrolled in Payer Authentication. Please authenticate the cardholder before continuing with the transaction. 

        :param message: The message of this RiskV1AuthenticationsPost201Response.
        :type: str
        """

        self._message = message

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this RiskV1AuthenticationsPost201Response.

        :return: The client_reference_information of this RiskV1AuthenticationsPost201Response.
        :rtype: Ptsv2payoutsClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this RiskV1AuthenticationsPost201Response.

        :param client_reference_information: The client_reference_information of this RiskV1AuthenticationsPost201Response.
        :type: Ptsv2payoutsClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def order_information(self):
        """
        Gets the order_information of this RiskV1AuthenticationsPost201Response.

        :return: The order_information of this RiskV1AuthenticationsPost201Response.
        :rtype: RiskV1AuthenticationsPost201ResponseOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this RiskV1AuthenticationsPost201Response.

        :param order_information: The order_information of this RiskV1AuthenticationsPost201Response.
        :type: RiskV1AuthenticationsPost201ResponseOrderInformation
        """

        self._order_information = order_information

    @property
    def consumer_authentication_information(self):
        """
        Gets the consumer_authentication_information of this RiskV1AuthenticationsPost201Response.

        :return: The consumer_authentication_information of this RiskV1AuthenticationsPost201Response.
        :rtype: RiskV1AuthenticationsPost201ResponseConsumerAuthenticationInformation
        """
        return self._consumer_authentication_information

    @consumer_authentication_information.setter
    def consumer_authentication_information(self, consumer_authentication_information):
        """
        Sets the consumer_authentication_information of this RiskV1AuthenticationsPost201Response.

        :param consumer_authentication_information: The consumer_authentication_information of this RiskV1AuthenticationsPost201Response.
        :type: RiskV1AuthenticationsPost201ResponseConsumerAuthenticationInformation
        """

        self._consumer_authentication_information = consumer_authentication_information

    @property
    def error_information(self):
        """
        Gets the error_information of this RiskV1AuthenticationsPost201Response.

        :return: The error_information of this RiskV1AuthenticationsPost201Response.
        :rtype: PtsV2PaymentsPost201ResponseErrorInformation
        """
        return self._error_information

    @error_information.setter
    def error_information(self, error_information):
        """
        Sets the error_information of this RiskV1AuthenticationsPost201Response.

        :param error_information: The error_information of this RiskV1AuthenticationsPost201Response.
        :type: PtsV2PaymentsPost201ResponseErrorInformation
        """

        self._error_information = error_information

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
        if not isinstance(other, RiskV1AuthenticationsPost201Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
