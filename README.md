# Uncommon `env` Keys in Laravel


## What is this?

As you might have read on [laravel documentation](https://laravel.com/docs/5.6/configuration#environment-configuration):  
  

> Your `.env` file should not be committed to your application's source control, since each developer / server using your application could require a different environment configuration. Furthermore, this would be a security risk in the event an intruder gains access to your source control repository, since any sensitive credentials would get exposed.

> If you are developing with a team, you may wish to continue including a `.env.example` file with your application. By putting place-holder values in the example configuration file, other developers on your team can clearly see which environment variables are needed to run your application.

You may forget to add some keys to the `.env.example` file, while it is added on the `.env` file and not even committed, because of the source control considerations. This repository helps you find the uncommon keys between `.env` and `.env.example` files, no need to double-check it by eyes.

## How to use this code with laravel?
```
$ cd path/to/your/laravel/project/

$ echo 'find_uncommon_env_keys.py' >> .gitignore

$ wget https://raw.githubusercontent.com/MajidAlaeinia/uncommon-env-keys-finder/master/find_uncommon_env_keys.py

$ python find_uncommon_env_keys.py
```
  

That's it.

## TODO
- [ ] Determine which key is from which file (.env or .env.example).  
- [ ] Php Equivalent Implementation.  
- [ ] Bash Implementation with `diff`.
