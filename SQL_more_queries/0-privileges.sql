-- listing privileges of mysql users
-- comment
/*
#!/bin/bash
USERS = ('user_0d_1' 'user_0d_2')
HOST = 'localhost'

for USER in '${USERS[@]}'
do
	SHOW GRANTS FOR '$USER'@'$HOST';
done
*/
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
