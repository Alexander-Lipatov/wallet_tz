# JavaCode - ТЗ

- Тестовое задание на позицию “Python разработчика” в компанию JavaCode.
  
- Требуется написать приложение, которое по REST принимает запрос вида <b>POST api/v1/wallets/<WALLET_UUID>/operation</b>
  
```
{
  operationType: DEPOSIT or WITHDRAW,
  amount: 1000
}
```

- Выполнить логику по изменению счета в базе данных

- Иметь возможность получить баланс кошелька <b>GET api/v1/wallets/{WALLET_UUID}</b>
.
- ТЗ - [ссылка](https://docs.google.com/document/d/1hEnCQnhljJ-pAwg7coi31J_3A05ctPcysIdkIuHXRqs/edit?tab=t.0)
- Стек (Python, Django)

## 1. Клонируйте репозиторий
  
```
git clone https://github.com/Alexander-Lipatov/wallet_tz.git
```

## 2. Выполнить

```
cd wallet_tz
docker-compose build
docler-compose up
```

### Автор

- Липатов Александр (ТГ [@Lipatov1993](https://t.me/lipatov1993), GitHub [Alexander-Lipatov](https://github.com/Alexander-Lipatov)
