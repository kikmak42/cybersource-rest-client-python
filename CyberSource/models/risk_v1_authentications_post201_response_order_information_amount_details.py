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


class RiskV1AuthenticationsPost201ResponseOrderInformationAmountDetails(object):
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
        'currency': 'str'
    }

    attribute_map = {
        'currency': 'currency'
    }

    def __init__(self, currency=None):
        """
        RiskV1AuthenticationsPost201ResponseOrderInformationAmountDetails - a model defined in Swagger
        """

        self._currency = None

        if currency is not None:
          self.currency = currency

    @property
    def currency(self):
        """
        Gets the currency of this RiskV1AuthenticationsPost201ResponseOrderInformationAmountDetails.
        Currency used for the order. Use the three-character I[ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)  For details about currency as used in partial authorizations, see \"Features for Debit Cards and Prepaid Cards\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your payment authorization request.  #### DCC for First Data Your local currency. For details, see the `currency` field description in [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf). 

        :return: The currency of this RiskV1AuthenticationsPost201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this RiskV1AuthenticationsPost201ResponseOrderInformationAmountDetails.
        Currency used for the order. Use the three-character I[ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)  For details about currency as used in partial authorizations, see \"Features for Debit Cards and Prepaid Cards\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your payment authorization request.  #### DCC for First Data Your local currency. For details, see the `currency` field description in [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf). 

        :param currency: The currency of this RiskV1AuthenticationsPost201ResponseOrderInformationAmountDetails.
        :type: str
        """
        if currency is not None and len(currency) > 3:
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")

        self._currency = currency

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
        if not isinstance(other, RiskV1AuthenticationsPost201ResponseOrderInformationAmountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
