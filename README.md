# CyberSecurity-Project
Project Overview :

Virgin Australia is Australia’s second-largest airline and is very popular for its distinctive branding and innovative service offerings. Its headquarters is in Brisbane, and it operates a domestic and international flight network. Virgin Australia's fleet primarily consists of Boeing and Airbus aircraft, servicing a network of domestic and international destinations. Despite its challenges, Virgin Australia remains committed to providing high-quality service and innovation, aiming to remain a key player in the competitive aviation market.

To improve the quality-of-service Virgin Australia takes the initiative to track on-time performance and compare it against other airlines. We seek help from different vendors who can develop a website and help Virgin keep track of the information. The website should be secure, highly scalable, and free from distributed Denial of Service (DDOS) attacks. Virgin Australia uses AWS as its cloud vendor to deploy cloud resources, so the infrastructure should be developed based on AWS cloud.

Milestones: Provide at least two architectures for the overall design and recommend the best solution to establish and maintain a multi-tier web application in AWS that is secure, scalable, and leverages AWS networking and security services.

Outputs include:

Architecture Diagram with implementation strategy with timeline which includes:
o   Full project strategy

o   Infrastructure and development cost

o   Pen testing

o   Timeline

o   Security assessment

Steps to implement with the following details:
o   Design and Create VPC

o   Setup NACL (Network Access Control List)

o   Configure DNS and CDN

o   Deploy Application in EC2

A POC (Proof of Concept) in AWS
Technical background (or specification or knowledge) requirements [100-200 words]:

• Amazon VPC (Virtual Private Cloud): Create a custom VPC to isolate your web application infrastructure in a virtual network that you define. Utilize public and private subnets to separate your application's front-end and back-end components.

• Amazon EC2 (Elastic Compute Cloud): Deploy web servers in the public subnet and database servers in the private subnet. Use EC2 instances to host your application code and database.

• Amazon RDS (Relational Database Service): Use RDS for a managed database service in the private subnet, enhancing security by restricting direct internet access.

• Elastic Load Balancing (ELB): Deploy an ELB in the public subnet to distribute incoming traffic across multiple EC2 instances, improving the fault tolerance of your application.

• Amazon CloudFront: Implement CloudFront as a content delivery network (CDN) to cache your web content closer to your users, reducing latency and improving load times.

• AWS WAF (Web Application Firewall): Integrate AWS WAF with CloudFront to protect your web application from common web exploits and bots that could affect availability, compromise security, or consume excessive resources.

• Amazon Route 53: Use Route 53 for DNS management, routing users to your application in a reliable and cost-effective way.

• AWS Identity and Access Management (IAM): Manage access to AWS services and resources securely. Use IAM roles and policies to grant precise permissions to AWS resources and users.

• AWS Shield: Protect your web application from DDoS attacks with AWS Shield, especially if your application is public-facing and requires high availability.

