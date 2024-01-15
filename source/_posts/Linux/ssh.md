---
toc: true
url: ssh
covercopy: © DALLE 3
priority: 10000
date: 2023-12-20 11:59:14
title: "Secure Shell (SSH)"
ytitle: "Secure Shell (SSH)"
description: "Secure Shell (SSH) installation, usage, and trouble shooting"
excerpt: "SSH, or Secure Shell, is a cryptographic network protocol for secure and encrypted communication over unsecured networks. It is significant for its ability to provide secure remote access to servers, secure file transfer, and a reliable means of executing remote commands, all while ensuring the confidentiality and integrity of data in transit."
tags: [Linux, bash, CLI Tools]
category: [Linux, System]
cover: "https://imgur.com/jDUCRCx.png"
thumbnail: "https://imgur.com/jDUCRCx.png"
---

## SSH

SSH, short for Secure Shell, is a network protocol used to securely access and manage a computer over an unsecured network. It provides a secure channel over an unencrypted network, like the internet, allowing users to log into another computer, execute commands remotely, and move files. SSH uses strong encryption to protect the data being transmitted, ensuring confidentiality and integrity of the data against eavesdropping and interception. It's commonly used by system administrators and IT professionals for managing systems and applications remotely.

## How to Use It

Using SSH typically involves two primary components: an SSH client and an SSH server. The server runs on the machine you want to connect to, while the client runs on the machine you're connecting from. Here's a basic guide on how to use SSH:

### Setting Up an SSH Server

1. **Install SSH Server**: On the remote machine (the one you want to access), you need to install an SSH server. For Linux systems, this is often done using the `openssh-server` package.

   ```bash
   sudo apt update
   sudo apt install openssh-server
   ```

   This example is for Debian-based systems (like Ubuntu). The commands might vary for other systems.

2. **Start and Enable SSH Service**: Ensure that the SSH service is started and enabled to start on boot.

   ```bash
   sudo systemctl start ssh
   sudo systemctl enable ssh
   ```

3. **Configure SSH Server (Optional)**: You can configure your SSH server by editing the `/etc/ssh/sshd_config` file. This step is optional and typically only necessary for advanced configurations.

### Connecting Using an SSH Client

1. **Install SSH Client**: Most Unix-like systems (Linux, macOS) come with an SSH client pre-installed. For Windows, you can use clients like PuTTY or use the built-in SSH client in Windows 10/11.

2. **Establish an SSH Connection**: To connect to the SSH server, you need the IP address or hostname of the server and the username on that system. The basic command is:

   ```bash
   ssh [username]@[host]
   ```

   For example, if your username is `user` and the server's IP address is `192.168.1.100`, you would use:

   ```bash
   ssh user@192.168.1.100
   ```

3. **Authenticate**: When you connect for the first time, you'll be asked to verify the identity of the server. After accepting, you'll be prompted for the password of the user account you are logging into on the remote machine.

4. **Using SSH**: Once connected, you can execute commands on the remote machine as if you were physically present. 

5. **Transferring Files (Optional)**: SSH also allows for secure file transfer using SCP or SFTP. 

   - To copy a file from your local machine to the remote machine:
     ```bash
     scp /path/to/local/file user@192.168.1.100:/path/to/remote/directory
     ```
   - To copy a file from the remote machine to your local machine:
     ```bash
     scp user@192.168.1.100:/path/to/remote/file /path/to/local/directory
     ```

6. **Exiting SSH**: To end your SSH session, simply type `exit` or press `Ctrl+D`.

## Configure file

`vim ~/.ssh/config`

<pre>
Host home_pc
    HostName 192.168.3.1
    User john
    Port 2322
</pre>

How to login this host:
`ssh home_pc`


### Security Considerations

- **SSH Keys**: For better security, it’s recommended to use SSH keys instead of passwords. SSH keys are a pair of cryptographic keys that can be used to authenticate to an SSH server as an alternative to password-based logins.
  
- **Firewall Settings**: Make sure your firewall settings allow SSH connections (usually on port 22).

- **Regular Updates**: Keep the SSH server software up to date for security.

SSH is a powerful tool for remote administration, but it's important to use it securely to protect your systems and data.

## SSH Key

Generating an SSH key is a security practice for authenticating to an SSH server more securely than using just a password. Here's why you should do it and how to generate an SSH key:

### Why Use SSH Keys?

1. **Enhanced Security**: SSH keys are cryptographic keys that are much more secure than passwords. They are almost impossible to decipher using brute force methods.

2. **No Need for Passwords**: When you use SSH keys, you don't need to enter your password every time you connect, which reduces the risk of password theft.

3. **Automation Friendly**: SSH keys are ideal for automated processes. Scripts and applications can authenticate without manual password entry.

4. **Access Control**: SSH keys can be used to control who can access a server. Only users with the matching private key can access the server configured with the public key.

### How to Generate an SSH Key

#### On Linux or macOS:

1. **Open Terminal**: Launch the terminal application.

2. **Generate Key Pair**: Use the `ssh-keygen` command to generate a new SSH key pair.

   ```bash
   ssh-keygen -t rsa -b 4096
   ```

   This command creates a new SSH key using the RSA algorithm with a key size of 4096 bits, providing a good balance between security and compatibility. You can choose other algorithms like `ed25519` which is considered more secure but may not be compatible with older systems.

3. **Specify File to Save the Key**: By default, `ssh-keygen` will save the key in the `~/.ssh/id_rsa` file. You can specify a different file if you want.

4. **Enter a Passphrase (Optional)**: For additional security, you can enter a passphrase when prompted. This passphrase will be required whenever the private key is used.

### Adding the SSH Key to Your SSH Server

1. **Copy Public Key**: After generating your SSH key, you need to add the public key to the `~/.ssh/authorized_keys` file on your SSH server.

2. **Use `ssh-copy-id` on Linux/macOS**: If you're using Linux or macOS, you can use `ssh-copy-id` to copy your public key to the server easily.

   ```bash
   ssh-copy-id user@server-address
   ```

3. **Manual Copying**: If `ssh-copy-id` isn't available or you're using Windows, you can manually copy the public key text and append it to `~/.ssh/authorized_keys` on the server.

Remember, never share your private key. The public key is what you distribute or add to servers, while the private key should be securely stored and kept private.

## Trouble Shooting: Public Key Doesn't Work

If your SSH public key authentication isn't working, there could be several reasons. Here's a troubleshooting guide to help you resolve common issues:

### 1. Check File Permissions
- **On the Server**: SSH is particular about file permissions for the `~/.ssh` directory and the `authorized_keys` file. Incorrect permissions can prevent SSH from authenticating using keys.
  - The `~/.ssh` directory should have permissions set to `700` (drwx------).
  - The `authorized_keys` file should have permissions set to `600` (-rw-------).
  - Use the `chmod` command to set these permissions:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

### 2. Ensure Correct Ownership

The `.ssh` directory and the `authorized_keys` file should be owned by the user, not root or any other user. Use the `chown` command to set the ownership:

```bash
chown -R your_username:your_username ~/.ssh
```

You can also make sure that the home directory permissions are restricted to the user. I think it could do the same thing.

```bash
chmod -R u+rwX,go-rwx /home/your_username
```

### 3. Verify the Public Key Format

Ensure that the public key in `authorized_keys` is in the correct format. It should be a single line starting with `ssh-rsa` or `ssh-ed25519`, followed by the key, and optionally a comment.

### 4. Check the SSH Server Configuration

The SSH server configuration file (`/etc/ssh/sshd_config`) on the server might restrict public key authentication. Check the following settings:
  - `PubkeyAuthentication yes` should be set to allow public key authentication.
  - `AuthorizedKeysFile` should point to the correct path, typically `.ssh/authorized_keys`.
  - If `PasswordAuthentication` is set to `no`, the server will not fall back to password authentication if key authentication fails.
  - After making changes, restart the SSH service:

```bash
sudo systemctl restart ssh
```

### 5. Check SSH Client Configuration

On your client machine, ensure you're specifying the correct private key. If you're using a key with a non-default name or location, specify it with the `-i` option:

```bash
ssh -i /path/to/private_key user@server
```

### 6. Look at Server Logs

SSH server logs can provide details on why the key authentication is failing. Check the logs for relevant error messages:
  - On most Linux systems, SSH logs are located in `/var/log/auth.log` or `/var/log/secure`.

### 7. Validate Key Pair

Ensure that the public and private keys are a matching pair. If you have regenerated or changed keys, make sure the server has the corresponding public key.

### 8. Check Passphrase

If your private key is protected with a passphrase, ensure you're entering the correct passphrase when prompted.

### 9. Network Issues

Confirm there are no network issues preventing SSH access. Firewall settings on either the client or server side can block SSH connections.

### 10. Client-Side Debugging

Use SSH with the `-vvv` option for verbose output, which can give more insights:

```bash
ssh -vvv -i /path/to/private_key user@server
```

This will provide detailed debug information about each step of the SSH connection process, potentially highlighting where the issue lies.


<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
