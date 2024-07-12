import subprocess

class Powershell:
    '''Powershell scripts defined inside each Python function in order to simplify tasks in the Active Directory.'''
    def __init__(self):
        pass

    def create_ADUser(full_name, name, surname, account_name, username_in_domain, sector, domain, password, description):
        user = f'''Import-Module ActiveDirectory; New-ADUser -Name "{full_name}; -GivenName "{name}"; -Surname {surname}; -SamAccountName "{account_name}"; -UserPrincipalName "{username_in_domain}"; -Path "OU={sector}, DC={domain}, DC=com, DC=br"; -AccountPassword (ConvertTo-SecureString "{password}" -AsPlainText -Force); -Enabled $true; -Description "{description}";
        '''
        create_user = subprocess.run(['powershell', '-Command', user], capture_output=True, text=True)

        print(create_user.stdout)

        if create_user.stderr:
            print(f'Erros: {create_user.stderr}')

    def disable_ADUser(ad_user):
        disable_user = subprocess.run(['powershell', '-Command', f'Import-Module ActiveDirectory; Disable-ADAccount -Identity {ad_user};'], capture_output=True, text=True)

        print(disable_user.stdout)

        if disable_user.stderr:
            print(f'Erros: {disable_user.stderr}')


    def enable_ADUser(ad_user):
        enable_user = subprocess.run(['powershell', '-Command', f'Import-Module ActiveDirectory; Enable-ADAccount -Identity {ad_user}'], capture_output=True, text=True)

        print(enable_user.stdout)

        if enable_user.stderr:
            print(f'Erros: {enable_user.stderr}')


    def unlock_ADUser(ad_user):
        unlock_user = subprocess.run(['powershell', '-Command', f'Import-Module ActiveDirectory; Unlock-ADAccount -Identity {ad_user}'], capture_output=True, text=True)

        print(unlock_user.stdout)

        if unlock_user.stderr:
            print(f'Erros: {unlock_user.stderr}')


    def change_password_next_logon(ad_user):
        change_pass = subprocess.run(['powershell', '-Command', f'Import-Module ActiveDirectory; Set-ADUser -Identity {ad_user} -ChangePasswordAtLogon $true'], capture_output=True, text=True)

        print(change_pass.stdout)

        if change_pass.stderr:
            print(f'Erros: {change_pass.stderr}')


    def remove_computer_from_AD(ad_computer):
        remove = subprocess.run(['powershell', '-Command', f'Import-Module ActiveDirectory; Remove-ADComputer -Identity "{ad_computer}"'], capture_output=True, text=True)

        print(remove.stdout)

        if remove.stderr:
            print(f'Erros: {remove.stderr}')


    def add_computer_to_group(ad_computer, ad_group):
        add_computer = subprocess.run(['powershell', '-Command', f'Import-Module ActiveDirectory; Add-ADGroupMember -Identity "{ad_group}" -Members "{ad_computer}"'], capture_output=True, text=True)

        print(add_computer.stdout)

        if add_computer.stderr:
            print(f'Erros: {add_computer.stderr}')


    def add_member_to_group(ad_group, ad_user):
        add_member = subprocess.run(['powershell', '-Command', f'Add-ADGroupMember -Identity "{ad_group}" -Members "{ad_user}"'], capture_output=True, text=True)

        print(add_member.stdout)

        if add_member.stderr:
            print(f'Erros: {add_member.stderr}')

    def remove_user_from_group(ad_group, ad_user):
        remove_user = subprocess.run(['powershell', '-Command', f'Import-Module ActiveDirectory; Remove-ADGroupMember -Identity "{ad_group}" -Members "{ad_user}";'], capture_output=True, text=True)

        print(remove_user.stdout)

        if remove_user.stderr:
            print(f'Erros: {remove_user.stderr}')    

    def greet_user(ad_user):
        greet = subprocess.run(['powershell', '-Command', f'Import-Module ActiveDirectory; Write-Output "Hello, {ad_user}! Welcome to San Andreas!"'], capture_output=True, text=True)
    
        print(greet.stdout)

        if greet.stderr:
            print(f'Erros: {greet.stderr}')

    def export_userdata_from_ad_to_csv(csv_path):
        path = f'$csvPath = "{csv_path}' + r'\Ad_users.csv"'
        query = '$users = Get-ADUser -Filter * -Properties Name, DistinguishedName, Enabled | Where-Object {$_.Enabled -eq $true} | Select-Object Name, DistinguishedName'
        userdata_extraction = """foreach ($user in $users) {
        $ou = ($user.DistinguishedName -split “,”, 2)[1] -replace 'OU=',''
        $user | Add-Member -MemberType NoteProperty -Name OU -Value $ou
        }
        """
        export_to_csv = '$users | Export-Csv -Path $csvPath -NoTypeInformation'

        full_command = f'Import-Module ActiveDirectory; {path}; {query}; {userdata_extraction}; {export_to_csv};'

        export = subprocess.run(['powershell', '-Command', full_command], capture_output=True, text=True)

        print(export.stdout)

        if export.stderr:
            print(f'Erros: {export.stderr}')

    def import_userdata_from_csv_to_AD():
        print('Olá!')

    def edit_userdata_by_csv():
        print('Olá!')
