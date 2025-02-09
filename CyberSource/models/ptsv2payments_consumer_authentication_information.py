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


class Ptsv2paymentsConsumerAuthenticationInformation(object):
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
        'cavv': 'str',
        'cavv_algorithm': 'str',
        'eci_raw': 'str',
        'pares_status': 'str',
        'veres_enrolled': 'str',
        'xid': 'str',
        'ucaf_authentication_data': 'str',
        'ucaf_collection_indicator': 'str'
    }

    attribute_map = {
        'cavv': 'cavv',
        'cavv_algorithm': 'cavvAlgorithm',
        'eci_raw': 'eciRaw',
        'pares_status': 'paresStatus',
        'veres_enrolled': 'veresEnrolled',
        'xid': 'xid',
        'ucaf_authentication_data': 'ucafAuthenticationData',
        'ucaf_collection_indicator': 'ucafCollectionIndicator'
    }

    def __init__(self, cavv=None, cavv_algorithm=None, eci_raw=None, pares_status=None, veres_enrolled=None, xid=None, ucaf_authentication_data=None, ucaf_collection_indicator=None):
        """
        Ptsv2paymentsConsumerAuthenticationInformation - a model defined in Swagger
        """

        self._cavv = None
        self._cavv_algorithm = None
        self._eci_raw = None
        self._pares_status = None
        self._veres_enrolled = None
        self._xid = None
        self._ucaf_authentication_data = None
        self._ucaf_collection_indicator = None

        if cavv is not None:
          self.cavv = cavv
        if cavv_algorithm is not None:
          self.cavv_algorithm = cavv_algorithm
        if eci_raw is not None:
          self.eci_raw = eci_raw
        if pares_status is not None:
          self.pares_status = pares_status
        if veres_enrolled is not None:
          self.veres_enrolled = veres_enrolled
        if xid is not None:
          self.xid = xid
        if ucaf_authentication_data is not None:
          self.ucaf_authentication_data = ucaf_authentication_data
        if ucaf_collection_indicator is not None:
          self.ucaf_collection_indicator = ucaf_collection_indicator

    @property
    def cavv(self):
        """
        Gets the cavv of this Ptsv2paymentsConsumerAuthenticationInformation.
        Cardholder authentication verification value (CAVV).

        :return: The cavv of this Ptsv2paymentsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._cavv

    @cavv.setter
    def cavv(self, cavv):
        """
        Sets the cavv of this Ptsv2paymentsConsumerAuthenticationInformation.
        Cardholder authentication verification value (CAVV).

        :param cavv: The cavv of this Ptsv2paymentsConsumerAuthenticationInformation.
        :type: str
        """
        if cavv is not None and len(cavv) > 40:
            raise ValueError("Invalid value for `cavv`, length must be less than or equal to `40`")

        self._cavv = cavv

    @property
    def cavv_algorithm(self):
        """
        Gets the cavv_algorithm of this Ptsv2paymentsConsumerAuthenticationInformation.
        Algorithm used to generate the CAVV for Visa Secure or the UCAF authentication data for Mastercard Identity Check. 

        :return: The cavv_algorithm of this Ptsv2paymentsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._cavv_algorithm

    @cavv_algorithm.setter
    def cavv_algorithm(self, cavv_algorithm):
        """
        Sets the cavv_algorithm of this Ptsv2paymentsConsumerAuthenticationInformation.
        Algorithm used to generate the CAVV for Visa Secure or the UCAF authentication data for Mastercard Identity Check. 

        :param cavv_algorithm: The cavv_algorithm of this Ptsv2paymentsConsumerAuthenticationInformation.
        :type: str
        """
        if cavv_algorithm is not None and len(cavv_algorithm) > 1:
            raise ValueError("Invalid value for `cavv_algorithm`, length must be less than or equal to `1`")

        self._cavv_algorithm = cavv_algorithm

    @property
    def eci_raw(self):
        """
        Gets the eci_raw of this Ptsv2paymentsConsumerAuthenticationInformation.
        Raw electronic commerce indicator (ECI). For the description and requirements, see \"Payer Authentication,\" page 180.

        :return: The eci_raw of this Ptsv2paymentsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._eci_raw

    @eci_raw.setter
    def eci_raw(self, eci_raw):
        """
        Sets the eci_raw of this Ptsv2paymentsConsumerAuthenticationInformation.
        Raw electronic commerce indicator (ECI). For the description and requirements, see \"Payer Authentication,\" page 180.

        :param eci_raw: The eci_raw of this Ptsv2paymentsConsumerAuthenticationInformation.
        :type: str
        """
        if eci_raw is not None and len(eci_raw) > 2:
            raise ValueError("Invalid value for `eci_raw`, length must be less than or equal to `2`")

        self._eci_raw = eci_raw

    @property
    def pares_status(self):
        """
        Gets the pares_status of this Ptsv2paymentsConsumerAuthenticationInformation.
        Payer authentication response status. For the description and requirements, see \"Payer Authentication,\" page 180. 

        :return: The pares_status of this Ptsv2paymentsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._pares_status

    @pares_status.setter
    def pares_status(self, pares_status):
        """
        Sets the pares_status of this Ptsv2paymentsConsumerAuthenticationInformation.
        Payer authentication response status. For the description and requirements, see \"Payer Authentication,\" page 180. 

        :param pares_status: The pares_status of this Ptsv2paymentsConsumerAuthenticationInformation.
        :type: str
        """
        if pares_status is not None and len(pares_status) > 1:
            raise ValueError("Invalid value for `pares_status`, length must be less than or equal to `1`")

        self._pares_status = pares_status

    @property
    def veres_enrolled(self):
        """
        Gets the veres_enrolled of this Ptsv2paymentsConsumerAuthenticationInformation.
        Verification response enrollment status. For the description and requirements, see \"Payer Authentication,\" page 180.

        :return: The veres_enrolled of this Ptsv2paymentsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._veres_enrolled

    @veres_enrolled.setter
    def veres_enrolled(self, veres_enrolled):
        """
        Sets the veres_enrolled of this Ptsv2paymentsConsumerAuthenticationInformation.
        Verification response enrollment status. For the description and requirements, see \"Payer Authentication,\" page 180.

        :param veres_enrolled: The veres_enrolled of this Ptsv2paymentsConsumerAuthenticationInformation.
        :type: str
        """
        if veres_enrolled is not None and len(veres_enrolled) > 1:
            raise ValueError("Invalid value for `veres_enrolled`, length must be less than or equal to `1`")

        self._veres_enrolled = veres_enrolled

    @property
    def xid(self):
        """
        Gets the xid of this Ptsv2paymentsConsumerAuthenticationInformation.
        Transaction identifier. For the description and requirements, see \"Payer Authentication,\" page 180.

        :return: The xid of this Ptsv2paymentsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._xid

    @xid.setter
    def xid(self, xid):
        """
        Sets the xid of this Ptsv2paymentsConsumerAuthenticationInformation.
        Transaction identifier. For the description and requirements, see \"Payer Authentication,\" page 180.

        :param xid: The xid of this Ptsv2paymentsConsumerAuthenticationInformation.
        :type: str
        """
        if xid is not None and len(xid) > 40:
            raise ValueError("Invalid value for `xid`, length must be less than or equal to `40`")

        self._xid = xid

    @property
    def ucaf_authentication_data(self):
        """
        Gets the ucaf_authentication_data of this Ptsv2paymentsConsumerAuthenticationInformation.
        Universal cardholder authentication field (UCAF) data.  For the description and requirements, see \"Payer Authentication,\" page 180. 

        :return: The ucaf_authentication_data of this Ptsv2paymentsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._ucaf_authentication_data

    @ucaf_authentication_data.setter
    def ucaf_authentication_data(self, ucaf_authentication_data):
        """
        Sets the ucaf_authentication_data of this Ptsv2paymentsConsumerAuthenticationInformation.
        Universal cardholder authentication field (UCAF) data.  For the description and requirements, see \"Payer Authentication,\" page 180. 

        :param ucaf_authentication_data: The ucaf_authentication_data of this Ptsv2paymentsConsumerAuthenticationInformation.
        :type: str
        """
        if ucaf_authentication_data is not None and len(ucaf_authentication_data) > 32:
            raise ValueError("Invalid value for `ucaf_authentication_data`, length must be less than or equal to `32`")

        self._ucaf_authentication_data = ucaf_authentication_data

    @property
    def ucaf_collection_indicator(self):
        """
        Gets the ucaf_collection_indicator of this Ptsv2paymentsConsumerAuthenticationInformation.
        Universal cardholder authentication field (UCAF) collection indicator.  For the description and requirements, see \"Payer Authentication,\" page 180.  **CyberSource through VisaNet**\\ The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP01 TCR7 - Position: 5 - Field: Mastercard Electronic Commerce Indicators—-UCAF Collection Indicator 

        :return: The ucaf_collection_indicator of this Ptsv2paymentsConsumerAuthenticationInformation.
        :rtype: str
        """
        return self._ucaf_collection_indicator

    @ucaf_collection_indicator.setter
    def ucaf_collection_indicator(self, ucaf_collection_indicator):
        """
        Sets the ucaf_collection_indicator of this Ptsv2paymentsConsumerAuthenticationInformation.
        Universal cardholder authentication field (UCAF) collection indicator.  For the description and requirements, see \"Payer Authentication,\" page 180.  **CyberSource through VisaNet**\\ The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP01 TCR7 - Position: 5 - Field: Mastercard Electronic Commerce Indicators—-UCAF Collection Indicator 

        :param ucaf_collection_indicator: The ucaf_collection_indicator of this Ptsv2paymentsConsumerAuthenticationInformation.
        :type: str
        """
        if ucaf_collection_indicator is not None and len(ucaf_collection_indicator) > 1:
            raise ValueError("Invalid value for `ucaf_collection_indicator`, length must be less than or equal to `1`")

        self._ucaf_collection_indicator = ucaf_collection_indicator

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
        if not isinstance(other, Ptsv2paymentsConsumerAuthenticationInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
