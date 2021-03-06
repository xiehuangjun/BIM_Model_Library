# BIM Model Library API User guide
###### tags: `BIM Model Library`

## Code
> GitHub: https://github.com/xiehuangjun/BIM_Model_Library.git
> 

## File structure
> ├── api.py

> ├── bim_file

> │   ├── BIM_API.postman_collection.json

> │   ├── Object.3dm

> │   ├── Object.gh

> │   ├── Object.png

> │   ├── Project1.jpg

> │   └── Project.jpg

> ├── config.ini

> ├── create_table

> │   └── create_table.py

> ├── Ethereum_Transaction.py

> ├── ethereum.txt

> ├── nohup.out

> ├── __pycache__

> │   ├── Ethereum_Transaction.cpython-36.pyc

> │   └── subfunction.cpython-36.pyc

> └── subfunction.py

> 

## Create a MySql DB
> Using docker to create MySql DB. 
> 1. `sudo apt-get install docker.io`
> 2. Use `sudo docker run -p 3308:3306 --name BIM_sql -e MYSQL_ROOT_PASSWORD=12345678 -d mysql` to create a MySql DB. 
> 3. Use `docker ps` to see the status of docker. 

## Create an ethereum
> 1. Use `mkdir ethereum` to create a new folder.
> 2. Use `cd ./ethereum` to change your location.
> 3. Use `geth --datadir test init ./genesis.json` to create an ethereum.
>
```yaml=1
{
  "config": {
    "chainId": 50885,
    "homesteadBlock": 0,
    "eip150Block": 0,
    "eip150Hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "eip155Block": 0,
    "eip158Block": 0,
    "byzantiumBlock": 0,
    "constantinopleBlock": 0,
    "petersburgBlock": 0,
    "istanbulBlock": 0,
    "ethash": {}
  },
  "nonce": "0x0",
  "timestamp": "0x5e64ebff",
  "extraData": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "gasLimit": "0x47b760",
  "difficulty": "0x80",
  "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "coinbase": "0x0000000000000000000000000000000000000000",
  "alloc": {},
  "number": "0x0",
  "gasUsed": "0x0",
  "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000"
}
```
> 4. Use `personal.newAccount("password")` to create a miner account. And it will return a AccountID back to you.
> 5. Use `personal.newAccount("password")` to create a user account. And it will return a AccountID back to you.
> 6. You can use the `eth.accounts` to list all account.
> 7. Use `miner.start()` start to dug.
> 8. After dug the coin, you can use `miner.stop` to stop dug.
> 9. Use `eth.getBalance(<miner account>)` to check the coin of miner account.



## Setting the config of python
> The config file is at BIM_API/cinfig.ini.
> 
```python=1
[MYSQL]
host = 140.118.121.100
port = 3307
user = root
password = 12345678

[FLASK]
host = 0.0.0.0
port = 5050

[PATH]
file_path = /home/zhongyu/data

[ETHEREUM]
host = 140.118.121.100
port = 30786
miner_account = 0xf74d0b361301b10e0625312f1a8202f453286744
miner_passwd = password
user = 0x9ac1ba1dfe605b2463728ae71181bbe0da58e9f2
```
> Accroding to your system setting to edit your config.ini.

## Iinitiate the DB
> In `BIM_API` use `python3 ./create_table/create_table.py` to initiate the DB.
> 

## Run the api
> In `BIM_API` use `python3 ./api.py` to run the api.
> 

## API Function

```
1. Register User information
POST : http://140.118.121.100:5050/register 
Rule: Body -> raw -> json
Parameters: 
{
  "User_accountID": "M10902208",
  "User_account_name": "HuangJun",
  "User_group": "A組",
  "User_password": "m10902208"
}
```
```
2. Login 
POST : http://140.118.121.100:5050/login
Rule: Body -> raw -> json
Parameters: 
{
  "User_accountID": "cc11",
  "User_password": "11"
}
```
```
3. Upload the information of Model Library (include text, files)
POST : http://140.118.121.100:5050/object_store
Rule: Body -> form-data (Key, Value)
Parameters: 
  a. User_accountID [text]
  b. Object_Name [text]
  c. opng [file]
  d. threedm [file]
  e. gh [file]
  f. pjpg [file]
  g. ojson [file]
  h. pdf [file]
```
```
4. According to the paramters, and get the information from the database
GET : http://140.118.121.100:5050/object_information
Rule: Params (Key, Value)
Parameters: 
  a. User_accountID [text]
  b. Object_Name [text]
  c. Object_ID [text]
```
```
5. Download the GH file.
GET : http://140.118.121.100:5050/gh_download
Rule: Params (Key, Value)
Parameters: 
  a. Object_ID [text]
```
```
6. Download the 3DM file.
GET : http://140.118.121.100:5050/3dm_download
Rule: Params (Key, Value)
Parameters: 
  a. Object_ID [text]
```
```
7. Get the all data from the database, and display on the Model Library Web.
GET : http://140.118.121.100:5050/main
```
```
8. According to the paramters, and search from the database
GET : http://140.118.121.100:5050/search
Rule: Params (Key, Value)
Parameters: 
  a. User_accountID [text]
  b. Object_Name [text]
```
```
9. Download the PDF file.
GET : http://140.118.121.100:5050/pdf_download
Rule: Params (Key, Value)
Parameters: 
  a. Object_ID [text]
```
```
11. Download the JSON file.
GET : http://140.118.121.100:5050/json_download
Rule: Params (Key, Value)
Parameters: 
  a. Object_ID [text]
```
```
12. Download the GH file of the Model Library, and use the Grasshopper to get the file.
POST : http://140.118.121.100:5050/ML_download_gh
Rule: Body -> form-data
Parameters: 
  a. Object_ID [text]
```
```
13. Download the 3dm file of the Model Library, and use the Grasshopper to get the file.
POST : http://140.118.121.100:5050/ML_download_3dm
Rule: Body -> form-data
Parameters: 
  a. Object_ID [text]
```
```
14. Download the ghuser file of the Model Library, and use the Grasshopper to get the file.
POST : http://140.118.121.100:5050/ML_download_ghuser
Rule: Body -> form-data
Parameters: 
  a. Object_ID [text]
```

> editor HJ 2021/07/09
