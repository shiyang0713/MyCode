#!/bin/bash

#首先輸入名字與性別
#再輸入體重與身高,程式計算BMI的值
#並根據輸入者的性別及BMI標準判斷給予建議

read -p "Enter your Name and Gender (male/female): " name gender

if [[ $gender == male ]]
then
	echo "$name is male"
elif [[ $gender == female ]]
then
	echo "$name is female"
else 
	echo "???"
fi	
read -p "Enter your weight and height(KG/M)" weight height
BMI=$(echo "$weight/($height*$height)" | bc )
 #"$weight/($height*$height)" 

echo "Hello $name , your BMI is $BMI " 

if [[ $gender == male ]]
then
	if (( 18 <= $BMI && $BMI <= 24 ))
	then
		echo 'keep going!'
	elif (( $BMI == 24 ))	
	then
		echo 'ideal ! '
	else 
		echo 'watch your weight!'
	fi
elif [[ $gender == female ]]
then
	if (( 18 <= $BMI && $BMI <= 24 )) && [[ $gender == female ]]
	then
		echo 'keep going!'
	elif (( $BMI == 22 ))	
	then
		echo 'ideal ! '
	else 
		echo 'watch your weight'
	fi
else
	echo 'PLEASE RETYPE YOUR GENDER !'
fi

