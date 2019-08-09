# TssV2TransactionsPost201Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_id** | **str** | An unique identification number assigned by CyberSource to identify each Search request. | [optional] 
**save** | **bool** | save or not save. | [optional] 
**name** | **str** | The description for this field is not available.  | [optional] 
**timezone** | **str** | Time Zone in ISO format. | [optional] 
**query** | **str** | transaction search query string. | [optional] 
**offset** | **int** | offset. | [optional] 
**limit** | **int** | Limit on number of results. | [optional] 
**sort** | **str** | A comma separated list of the following form - fieldName1 asc or desc, fieldName2 asc or desc, etc. | [optional] 
**count** | **int** | Results for this page, this could be below the limit. | [optional] 
**total_count** | **int** | Total number of results. | [optional] 
**status** | **str** | The status of the submitted transaction. | [optional] 
**submit_time_utc** | **str** | Time of request in UTC. Format: &#x60;YYYY-MM-DDThh:mm:ssZ&#x60; Example &#x60;2016-08-11T22:47:57Z&#x60; equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The &#x60;T&#x60; separates the date and the time. The &#x60;Z&#x60; indicates UTC.  | [optional] 
**embedded** | [**TssV2TransactionsPost201ResponseEmbedded**](TssV2TransactionsPost201ResponseEmbedded.md) |  | [optional] 
**links** | [**PtsV2PaymentsReversalsPost201ResponseLinks**](PtsV2PaymentsReversalsPost201ResponseLinks.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


