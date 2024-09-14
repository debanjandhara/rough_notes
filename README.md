# Wht I am Learning

- selenium.
- playing with large csv to excels, data manupulation
- ai chatbots, gradio, llms, hugging face
- deploying with vllm
- created a chatbot api endpoint with pygmallion , flask
- scaling flask with worker threads, gunzip
- rate limiting and asyncio in flassk
- queeuing using redis layer, Kafka, RabbitMQ
- multiinstance scale using nginx, and using 3rd part nginx tool, for proper load balancing
- nginx, config files, and sites available... with wokrer thread concept, and multiple port config for same application and default time out set for connection...
- node backend scaling using pm2, react hosting with serve and express code, and scaling with pm2 with express
- pm2 ecosystem.cjs, config.. for fork and cluster mode - and with restart
- git https authentication --> use token
- git ssh use .. learn about keys.. merge, conflict, stash, branch, checkout.. revert back
- multiple file server with worker threads, scaling, and restart
- working with opennebula
- Jenkins file, ansible, terraform, dockerfile, docker compose , lb nginx sonfiguration, nginx via docker.... mount disk to docker container env, portrainer

- ## Installation

* Create a python virtual environment: `python3.11 -m venv venv`
* Activate the virtual environment: `source venv/bin/activate`
* Install dependencies: `python3.11 -m pip install -r requirements.txt`



# DevOps Requirements

- Analyzing the business/technical requirement documents
- Contributing to the application design, development, testing, and deployment
- Participating in agile team meetings such as Stand-up calls and retrospective meetings
- Preparing the technical documentation required for the adopted SDLC process
- Collaborating with various State Street internal teams
- Cloud Computing – Understand IaaS, PaaS, SaaS, NaaS, and other AWS & Azure Cloud Computing Fundamentals
- DevOps – CI/CD concepts, Jenkins, Git, GitHub, Jenkins, Harness
- Monitoring Tools – Splunk/Dynatrace & Grafana for Presentation/Dashboards
- Site Reliability Engineering, ITIL Process (Ticketing & Project Management Tools – Service Now & Jira/Confluence)
- Database, Middleware, Storage, Windows, Unix operating environment concepts
- Automation Tools/Languages (R, Python, Ansible (AAAS), RPA – Blue Prism), Django for automation of N/w configurations
- Working knowledge and skills in GUI development with Java middle and databases back-end to create an end-to-end solution desirable.
- Understanding the software development lifecycle and software development common practices (code reviews, unit testing, etc.)
- Good understanding of SQL performance tuning techniques including query plan understanding and management, SQL tracing, DB stats, indexing techniques, etc., highly preferred
- Good in managing and resolving problems on a live production system.

- Requirements :
Bachelor’s in computer science or related discipline; or equivalent work experience
4-7 years of experience
Data structures and algorithms, object-oriented programming, databases, SQL, web programming, design patterns, SOLID principles, cloud technologies (AWS, Azure, etc.)
4+ years’ web development, Java frameworks (Spring/Quarkus)
3+ years’ REST/gRPC services, micro-services
3+ years’ unit testing, mocking frameworks, automation frameworks.
DevOps mindset – 3+ years’ experience in CI/CD, SDLC environment, implemented exception handling, logging, monitoring, performance measurement, operational metrics knowledge.
3+ years’ experience working in agile methodologies (Scrum, Kanban)
Strong communication, partnership, teamwork, and influencing skills required



**1. Introduction to GPT and LLMs (0:03 - 0:32)**
- GPT stands for Generative Pre-trained Transformer, a large language model.
- GPT is known for generating human-like text.
- The video will cover three key questions: What is an LLM, How do they work, and Business applications of LLMs.

**2. What is a Large Language Model (0:36 - 1:31)**
- Large language models are instances of foundation models.
- Foundation models are pre-trained on large amounts of unlabeled data.
- They learn from patterns in data to produce generalizable output.
- Large language models are applied to text and text-like data.
- They are trained on massive datasets, potentially petabytes of text data.
- Parameter count is significant, e.g., GPT-3 has 175 billion parameters.

**3. How Large Language Models Work (2:04 - 4:18)**
- LLMs are composed of three key components: data, architecture, and training.
- Data includes vast amounts of text data, while the architecture is based on the transformer neural network.
- Transformers understand context by considering each word in relation to others.
- During training, the model learns to predict the next word in a sentence.
- Fine-tuning on specific datasets helps LLMs become experts in particular tasks.

**4. Business Applications of LLMs (4:23 - 5:14)**
- Customer service applications can use LLMs for intelligent chatbots, handling various customer queries.
- Content creation can benefit from LLMs, generating articles, emails, social media posts, and video scripts.
- LLMs can contribute to software development by generating and reviewing code.
- The video concludes by noting that innovative applications continue to emerge as large language models evolve.

Feel free to add any additional content or specifics to these notes, and if you have any further questions or need more details on a particular section, please let me know.

https://betterprogramming.pub/speed-up-llm-inference-83653aa24c47 -->
https://www.youtube.com/watch?v=klTvEwg3oJ4&ab_channel=Fireship
In summary, the text provides optimization strategies for machine learning models:

1. **Precision Reduction**:
   - Using float16 or bfloat16 precision can speed up the model by approximately 20%.
   - It also reduces memory consumption by a factor of 2.

2. **Quantization**:
   - Employ 8-bit or 4-bit quantization to reduce memory usage by 2x or 3x.
   - Ideal for small devices with limited memory.
   - Note that quantization can degrade prediction quality.

3. **Fine-Tuning with Adapters**:
   - Utilize fine-tuning methods like LoRA and QLoRA to enhance prediction accuracy on your specific data.
   - Effective when combined with quantization.

4. **Tensor Parallelism**:
   - Implement tensor parallelism for faster inference on multiple GPUs, especially for running large models.

5. **Use Specialized Libraries**:
   - Consider using libraries designed for Large Language Model (LLM) inference and serving.
   - Examples include Text Generation Inference, DeepSpeed, or vLLM.
   - These libraries come with various optimization techniques, such as tensor parallelism, quantization, continuous batching, optimized CUDA kernels, and more.

These strategies aim to enhance the efficiency and performance of machine learning models while addressing concerns like memory consumption and prediction quality.


----- NETWROK ----

> > Difference b/t NAT and PAT

In NAT, Private IP addresses are translated into the public IP address. In PAT, Private IP addresses are translated into the public IP address via Port number.
go to instance >> security >> inbound >> allow all (to test at first), then stepwise allow 80 and special ports (8080 - Django, 5000 - Flask) to get access from outside
always browse by public ip of the instance, not the given instance ipv4 dns name (FQDN). Map this AWS ipv4 dns name and public ip in the registered dns server.


## What More to learn, take notes of...
- OS : Linux file strustures, permission, special commands - systemctl, act, vi, vim ,nano, cp -r, chmod -r, chown -r , update, upgrade , autoremove, purge all cache, lsof, net tools, docker commands,  (notes)
- OS THeory COncepts : registers, memeory alloc, deadlock, paging, page fault,
- Network : networking router, etc.. firewall,
- DBMS : Normalisation schema, joins, indexing, sql planner, layers of data flow.. how to play with big datas... basic sql queries... orms
- why which programming language, frameworks,... benefits.. advantages

-------------------------------------------------------------------------------------------



