# Riskv1authenticationsOrderInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_details** | [**Riskv1decisionsOrderInformationAmountDetails**](Riskv1decisionsOrderInformationAmountDetails.md) |  | [optional] 
**pre_order** | **str** | Indicates whether cardholder is placing an order with a future availability or release date. This field can contain one of these values: - MERCHANDISE_AVAILABLE: Merchandise available - FUTURE_AVAILABILITY: Future availability  | [optional] 
**pre_order_date** | **str** | Expected date that a pre-ordered purchase will be available. Format: YYYYMMDD  | [optional] 
**reordered** | **bool** | Indicates whether the cardholder is reordering previously purchased merchandise. This field can contain one of these values: - false: First time ordered - true: Reordered  | [optional] 
**ship_to** | [**Riskv1authenticationsOrderInformationShipTo**](Riskv1authenticationsOrderInformationShipTo.md) |  | [optional] 
**line_items** | [**list[Riskv1authenticationsOrderInformationLineItems]**](Riskv1authenticationsOrderInformationLineItems.md) | This array contains detailed information about individual products in the order. | [optional] 
**bill_to** | [**Riskv1authenticationsOrderInformationBillTo**](Riskv1authenticationsOrderInformationBillTo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


