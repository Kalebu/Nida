# [Nida](#)

Unofficial package for fetching users information based on National ID Number

## Installation

You can install it directly or using pip

Here how to install directly

```bash
git clone https://github.com/Kalebu/Nida
cd Nida
Nida -> python setup.y install
```

Here how to install from pip

```bash
pip install nida
```

## Usage

To fetch user information based on ID number do this;

```python
>>> from nida import load_user
>>> user_detail = load(national_id='XXXXXXXXX')
>>> print(user_datail)
user
{'Nin': 'XXXXXX', 'Firstname': 'XXXXXX', 'Middlename': 'XXXXXX', 'Surname': 'XXXXXX', 'Othernames': 'XXXXXX', 'Sex': 'XXXXXX', 'Dateofbirth': 'XXXXXX', 'Residentregion': 'XXXXXX', 'Residentdistrict': 'XXXXXX', 'Residentward': 'XXXXXX', 'Residentvillage': 'XXXXXX', 'Residentstreet': 'XXXXXX', 'Residentpostcode': 'XXXXXX', 'Permanentregion': 'XXXXXX', 'Permanentdistrict': 'XXXXXX', 'Permanentward': 'XXXXXX', 'Permanentvillage': 'XXXXXX', 'Permanentstreet': 'XXXXXX', 'Birthcountry': 'XXXXXX', 'Birthregion': 'XXXXXX', 'Birthdistrict': 'XXXXXX', 'Birthward': 'XXXXXX', 'Nationality': 'XXXXXX', 'Phonenumber': 'XXXXXX', 'Maritalstatus': 'XXXXXX', 'Occupation': 'XXXXXX', 'Primaryschooleducation': 'XXXXXX', 'Primaryschooldistrict': 'XXXXXX', 'Primaryschoolyear': 'XXXXXX', 'Photo': 'XXXXXX', 'Signature': 'XXXXXX', 'Nationalidnumber': 'XXXXXX', 'Lastname': 'XXXXXX'}
```

You can access user infromation by using keys and attributes just as shown below;

```python
>>> user_detetail['Firstname']
'XXXXXX'
>>> user_detail.get('Middlename')
'XXXXXX'
>>> user_detail.Lastname
'XXXXXX'
```

National ID Photo and Signature are auto converted into PIL Images and you can easily save save just as shown below;

```python
>>> user_detail.Photo.save('National_ID.png')
>>> user_detail.Signature.save('Signature.png')
```

If you want the data to be in the same from an API without any side effect preprocessing do this instead while loading user;

```python
>>> user_detail = load_user('xxxxxxxxxx', json = True)
>>> print(user_detail)
{
    ....
}
```

## Give it star

Did you find this repository useful to you ? Well then give it a star so as more people can get to know about it; 

## Issues

Are you facing any issue with usage of the package, just raise an issue and I looking to fixing it as soon as I can.

## Contributions

If there is anything yould would like to add warmly welcome, Jus fork it 

## Disclaimers

This is not an official package, therefore I'm not responsible for any misinformation or misuse of the package of any kind !!!

## Credits

All the credits to [Kalebu](https://github.com/Kalebu/) and [StackOverflow comment](https://stackoverflow.com/questions/53369396/how-to-integrate-national-identification-authority-nida-api-for-tanzania) from [dbrax](https://stackoverflow.com/users/6131960/emanuel-paul-mnzava)