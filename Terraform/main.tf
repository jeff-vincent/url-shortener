provider "aws" {
  region = "us-west-2"
  access_key = <your-access-key>
  secret_key = <your-secret-key>
}

resource "aws_vpc" "test-vpc" {
    cidr_block = "10.0.0.0/16"
    tags = {
        Name = "test-vpc"
    }
}

resource "aws_subnet" "subnet-1" {
    vpc_id = aws_vpc.test-vpc.id
    cidr_block = "10.0.1.0/24"
    availability_zone = "us-west-2a"
    tags = {
        Name = "test-subnet"
    }
}

resource "aws_internet_gateway" "gw" {
    vpc_id = aws_vpc.test-vpc.id
}

resource "aws_route_table" "r" {
    vpc_id = aws_vpc.test-vpc.id
    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.gw.id
    }
}

resource "aws_route_table_association" "a" {
    subnet_id = aws_subnet.subnet-1.id
    route_table_id = aws_route_table.r.id
}

resource "aws_security_group" "allow_web" {
    name = "allow_web_traffic"
    description = "Allow Web inbound traffic"
    vpc_id = aws_vpc.test-vpc.id

    ingress {
        description = "HTTPS"
        from_port = 443
        to_port = 443
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        description = "HTTP"
        from_port = 80
        to_port = 80
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        description = "SSH"
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_network_interface" "web-server-nic" {
    subnet_id = aws_subnet.subnet-1.id 
    private_ips = ["10.0.1.50"]
    security_groups = [aws_security_group.allow_web.id]
}

resource "aws_eip" "one" {
    vpc = true
    network_interface = aws_network_interface.web-server-nic.id 
    associate_with_private_ip = "10.0.1.50"
    depends_on = [aws_internet_gateway.gw]
}


resource "aws_instance" "ubuntu-web-server" {
    ami = "ami-02701bcdc5509e57b"
    instance_type = "t2.micro"
    availability_zone = "us-west-2a"
    key_name = "main"

    network_interface {
        device_index = 0
        network_interface_id = aws_network_interface.web-server-nic.id
    }

    tags = {
        Name = "ubuntu"
    }

    user_data = <<-EOF
                #!/bin/bash
                sudo snap install docker
                EOF
    }
