import nmap3
nmap = nmap3.Nmap()

ips = []

def soft_nmap():
    nmap.nmap_dns_brute_script("thecoder97.com")
    # if soft_test == None:
    #     pass
    # else:
    #     return soft_test

def main():
    soft_test = soft_nmap()
    if soft_test == None:
        print('Unsuccessful scan')
    else:
        print('Successful scan')
        print(soft_test['address'])

if __name__ == '__main__':
    main()


{
    "Version": "2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Action": "sts:AssumeRole",
        "Resource": "arn:aws:iam::864586846179:role/ec2readonlyaccess"
    }
}

{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "VisualEditor0",
			"Effect": "Allow",
			"Action": [
				"ec2:AuthorizeSecurityGroupEgress",
				"ec2:AuthorizeSecurityGroupIngress",
				"ec2:UpdateSecurityGroupRuleDescriptionsEgress",
				"ec2:DeleteTags",
				"ec2:CreateTags",
				"ec2:DescribeInstanceAttribute",
				"ec2:DescribeFleetInstances",
				"ec2:ModifySecurityGroupRules",
				"ec2:UpdateSecurityGroupRuleDescriptionsIngress",
				"ec2:RevokeSecurityGroupIngress",
				"ec2:CreateSecurityGroup",
				"ec2:RevokeSecurityGroupEgress",
				"ec2:DeleteSecurityGroup",
				"ec2:ApplySecurityGroupsToClientVpnTargetNetwork",
				"ec2:ModifyInstanceAttribute"
			],
			"Resource": [
				"arn:aws:ec2:*:853954225912:security-group-rule/*",
				"arn:aws:ec2:*:853954225912:security-group/sg-0a41fe8116d1f174a"
			]
		},
		{
			"Sid": "VisualEditor1",
			"Effect": "Allow",
			"Action": [
				"ec2:DescribeInstances",
				"ec2:DescribeIamInstanceProfileAssociations",
				"ec2:DescribeInstanceEventWindows",
				"ec2:DescribeInstanceEventNotificationAttributes",
				"ec2:DescribeSecurityGroups",
				"ec2:DescribeInstanceCreditSpecifications",
				"ec2:GetInstanceTypesFromInstanceRequirements",
				"ec2:DescribeSecurityGroupRules",
				"ec2:DescribeInstanceTypeOfferings",
				"ec2:DescribeSecurityGroupReferences",
				"ec2:DescribeInstanceTypes",
				"ec2:DescribeStaleSecurityGroups",
				"ec2:DescribeInstanceStatus",
				"ec2:CreateSecurityGroup"
			],
			"Resource": "*"
		}
	]
}