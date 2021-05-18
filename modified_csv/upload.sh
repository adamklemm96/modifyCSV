#!/bin/bash
link="/home/adam/today/ready"

for x in *csv
    do
        echo "$x"
        gcloud compute scp "$x" import-passwords:$link
        echo "$x uploaded to $link"

        read -p "Delete $x from modified_csv/ and downloaded_files/?[y/n]: " answer
        if [[ "$answer" == "y" ]]
            then
                rm "$x"
                #delete from downloaded files
                firstLetters=${x:0:4}
                rm ../downloaded_files/$firstLetters*.txt
                echo "Files removed from both directories"
        else:
            :
        fi
    done