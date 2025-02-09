# Ptsv2paymentsProcessingInformationRecurringOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loan_payment** | **bool** | Flag that indicates whether this is a payment towards an existing contractual loan.  Possible values: - &#x60;true&#x60;: Loan payment - &#x60;false&#x60;: (default) Not a loan payment See \&quot;Visa Debt Repayments,\&quot; page 218, for a list of processors that support this feature. For processor-specific details, see &#x60;debt_indicator&#x60; field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  | [optional] [default to False]
**first_recurring_payment** | **bool** | Flag that indicates whether this transaction is the first in a series of recurring payments.  This field is supported only for **Atos**, **FDC Nashville Global**, and **OmniPay Direct**.  Possible values:  - &#x60;true&#x60; Indicates this is the first payment in a series of recurring payments  - &#x60;false&#x60; (default) Indicates this is not the first payment in a series of recurring payments.  For more details, see \&quot;Recurring Payments,\&quot; page 198. For details, see &#x60;auth_first_recurring_payment&#x60; field description and \&quot;Recurring Payments\&quot; in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm)  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


