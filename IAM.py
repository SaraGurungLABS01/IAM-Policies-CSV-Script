import csv
import boto3

def export_iam_policies_to_csv(file_path):
    # create an IAM client
    iam_client = boto3.client('iam')

    # list IAM policies
    policies = iam_client.list_policies(Scope='All')['Policies']

    # specify the CSV file and its headers
    fieldnames = ['Policy Name', 'PolicyId', 'Arn']

    # create and open the CSV file for writing
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # iterate through policies and write to the CSV file
        for policy in policies:
            writer.writerow({
                'Policy Name': policy['PolicyName'],
                'PolicyId': policy['PolicyId'],
                'Arn': policy['Arn']
            })

if __name__ == '__main__':
    # specify the path for the CSV file
    file_path = 'iam_policies.csv'

    # ccall the function to export IAM policies to the CSV file
    export_iam_policies_to_csv(file_path)

    print(f'IAM policies exported to {file_path}')
