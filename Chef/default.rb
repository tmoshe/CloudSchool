#
# Cookbook:: main
# Recipe:: default
#
# Copyright:: 2023, The Authors, All Rights Reserved.



apt_package "python3" do
	action :install
end

apt_package "python3-pip" do
	action :install
end

apt_package "python3-requests" do
        action :install
end

apt_package "python3-flask" do
	action :install
end

git '/home/ubuntu/app' do
	repository 'https://github.com/tmoshe/CloudSchool.git'
	revision 'main'
	action :sync
end

execute "run-flask-apk'"  do
	command 'python3 app.py'
	cwd '/home/ubuntu/myApp/'
	user 'root'
	action :run
end

#python_package 'Flask' do
 # version '2.2.3'
#end

#file '/home/ubuntu/chef/hello.txt' do
 # content 'hello World!'
  #action :create
#end