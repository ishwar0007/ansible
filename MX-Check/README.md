# ansible-mx-check

1. All the servers must be defined in the host file present in the project files.
	To define the user of the host server - ansible_ssh_user=user
	To define the private key of the host server - ansible_ssh_private_key_file=key_path

2. To RUN the ansible run the following command:- ansible-playbook -i hosts playbook.yml

3. To run direct command on the host servers then use the following command - ansible -i ~/Documents/ansible/test_project/hosts  hello -m command -a "sudo killall screen"
