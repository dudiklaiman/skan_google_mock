from flask_smorest import abort
import json
from models import GoogleConfigModel, GoogleTokensModel


def google_leads_get_customer_client(req_data, version, id):
    """
    :param req_data:(headers)
    :param version:
    :param id: id can be customer id or customer client id
    :return: response according to given input
     """
    # check if version is not 15
    if version != '15':
        abort(400, message="wrong version")

    token_data = GoogleTokensModel.query.filter_by(short_live_token=req_data['Authorization'].split(" ")[0]).first()

    # if Login-Customer-Id exist in headers it means that param id is customer client id
    if "Login-Customer-Id" in list(req_data.keys()):
        fix_path = "{}.{}.{}.{}".format(token_data.app_id, token_data.network_user_id, req_data['Login-Customer-Id'],
                                        id)
        print(fix_path)

    # if not exist it means that param id is customer id
    else:
        fix_path = "{}.{}.{}".format(token_data.app_id, token_data.network_user_id, id)

    # we search for google_path in db
    data = GoogleConfigModel.query.filter_by(google_path=fix_path).all()

    # if param id is customer client id
    if "Login-Customer-Id" in list(req_data.keys()):

        # we iterate through all customer client ids data which contains in value the bucket id
        results = []
        for item in data:
            # all_path - app_id.network_user_id.customer_id.customer_client_id + item.value(bucket_id)
            all_path = fix_path + ".{}".format(json.loads(item.value))

            # bucket_data_dict contains value of row matching the full path
            # app_id.network_user_id.customer_id.customer_client_id.bucket_id
            bucket_data = GoogleConfigModel.query.filter_by(google_path=all_path).first()
            bucket_data_dict = json.loads(bucket_data.value)

            # building the final response
            final_data = {"segments": {
                "skAdNetworkAttributionCredit": bucket_data_dict['skAdNetworkAttributionCredit'],
                "skAdNetworkAdEventType": bucket_data_dict['skAdNetworkAdEventType'],
                "skAdNetworkPostbackSequenceIndex": bucket_data_dict['skAdNetworkPostbackSequenceIndex'],
                "skAdNetworkSourceType": bucket_data_dict['skAdNetworkSourceType'],
                "skAdNetworkUserType": bucket_data_dict['skAdNetworkUserType']
            },
                "campaign": {
                    "appCampaignSetting": {"appId": token_data.app_id},
                    # "name": bucket_data_dict["name"],
                    "resourceName": f"customers/{id}/campaigns/{json.loads(item.value)}",
                    "id": json.loads(item.value)
                },
                "metrics": {
                    "skAdNetworkTotalConversions": bucket_data_dict['skAdNetworkTotalConversions'],
                    "skAdNetworkInstalls": bucket_data_dict['skAdNetworkInstalls']
                }
            }
            results.append(final_data)
        return_data = {'results': results}


    # if param id is customer id return all customer client ids who are linked to customer id
    else:
        return_data = [{"customerClient": {
            "clientCustomer": f"customers/{id}",
            "resourceName": f"customers/{id}/customerClients/{json.loads(item.value)}"
        }} for item in data]

    return return_data
