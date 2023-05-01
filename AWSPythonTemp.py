import boto3
boto3.__version__
import pprint
import os

#new 4/12/23 - getting environmental variables
access_key = os.environ.get('AWS_ACCESS_KEY_ID')
secret_key = os.environ.get('AWS_ACCESS_KEY_ID')



#doesn't work, need the keys actually.
# s3 = boto3.client('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)

# Set up AWS credentials
# access_key = 
# secret_key = 
region_name = 'us-east-1'
s3_bucket = 'vladdybucket'
s3_bucket_public = 'vladdybucketpublic'

# Create S3 client
s3 = boto3.client('s3')
s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region_name)
s3_public = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region_name)

# Create a session instead of a client
session = boto3.Session(region_name=region_name, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
s3 = session.client('s3',aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# List all files in S3 - works
s3_result =  s3.list_objects_v2(Bucket=s3_bucket, Prefix="", Delimiter = "/")
pprint.pprint(s3_result)

#public version
s3_result_public =  s3_public.list_objects_v2(Bucket=s3_bucket_public, Prefix="", Delimiter = "/")
pprint.pprint(s3_result)



file_list = []
for item in s3_result['Contents']:
    file_list.append(item['Key'])
print(file_list)

file_list = []
for item in s3_result_public['Contents']:
    file_list.append(item['Key'])
print(file_list)


#GET LINKS FROM S3 WOO
#Note that Prefix is the subfolder here!!
s3_result_public =  s3_public.list_objects_v2(Bucket=s3_bucket_public, Prefix="stuff/", Delimiter = "/")

#JSON Parsing hell.
#list_objects_v2 returns a dictionary.
pprint.pprint(s3_result_public)
s3_result_public['Contents']
for item in s3_result_public['Contents']:
    print(item['Key'])

links = []
for obj in s3_result_public['Contents']:
    link = f"https://{s3_bucket_public}.s3.amazonaws.com/{obj['Key']}"
    links.append(link)


# Upload and Download file to S3
filename = r'C:\Users\Vlad\Desktop\python temp files\astronauts.csv'
key = r'astronauts_v2.csv'
s3.upload_file(filename, s3_bucket, key)
s3.download_file(s3_bucket, "people.txt", "people.txt")

# Upload and Download file to S3 public
filename = r'C:\Users\Vlad\Desktop\python temp files\astronauts.csv'
key_dont_do_this_way = r'/stuff/astronauts_v2.csv' #This way creates an empty folder called '/'
key_also_works = r'stuff/astronauts_v3.csv'
s3.upload_file(filename, s3_bucket_public, key)
s3.upload_file(filename, s3_bucket_public, key_also_works)
s3.download_file(s3_bucket, "people.txt", "people.txt")



Here, access_key and secret_key are your AWS access key ID and secret access key, respectively. region_name is the region where your S3 bucket is located, and s3_bucket is the name of the bucket where you want to upload the file.

The s3.upload_file() method is used to upload the file to S3. The first argument is the path to the local file you want to upload, the second argument is the name of the S3 bucket, and the third argument is the key or path you want to give to the file in the S3 bucket.

Note that you need to have the boto3 library installed in order to use it. You can install it using pip by running pip install boto3.
