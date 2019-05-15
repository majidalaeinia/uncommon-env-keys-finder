# Find uncommon keys between `.env` and `.env.example` files on laravel (yeah, by python)

As you might read on [laravel documentation](https://laravel.com/docs/5.6/configuration#environment-configuration):  
  

> Your `.env` file should not be committed to your application's source control, since each developer / server using your application could require a different environment configuration. Furthermore, this would be a security risk in the event an intruder gains access to your source control repository, since any sensitive credentials would get exposed.

> If you are developing with a team, you may wish to continue including a `.env.example` file with your application. By putting place-holder values in the example configuration file, other developers on your team can clearly see which environment variables are needed to run your application.

You might forget to add some keys to the `.env` file, while it is added on the `.env.example` file, because of the source control considerations. This repository makes you find the uncommon keys between `.env` and `.env.example` files, no need to double-check it by eyes.

## How to use this code with laravel
You may **just** copy [find_uncommon_env_keys.py](https://github.com/MajidAlaeinia/uncommon_env_keys_in_laravel/blob/master/find_uncommon_env_keys.py) to your root directory of your project, just where `.env` and `.env.example` are, then run:  
```python
python find_uncommon_env_keys.py
```

That's it.
