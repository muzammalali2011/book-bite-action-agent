import json
import boto3

bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        problem = body.get('problem', '')
        author = body.get('author', 'James Clear (Atomic Habits)')

        if not problem:
            return {
                'statusCode': 400,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({'error': 'No problem provided.'})
            }

        # Dynamic prompt engineering based on the selection
        if author == "General Advisor (Best Practices)":
            system_prompt = """
            You are a world-class life coach, productivity expert, and philosophy advisor. 
            You are speaking directly to a reader who needs your help.
            Your goal is to provide a highly actionable, zero-fluff solution to their problem using the best general self-help and psychology principles.
            
            Rules for your response:
            1. Be direct, empathetic, and highly practical.
            2. Keep it to a 1-minute read (under 250 words).
            3. Break the advice down into immediate, concrete steps.
            4. Do NOT introduce yourself. Just start giving the advice.
            5. Use Markdown formatting (bullet points, headers, bold text) to make it highly readable.
            """
        else:
            system_prompt = f"""
            You are {author}. You are speaking directly to a reader who needs your help.
            Your goal is to provide a highly actionable, zero-fluff solution to their problem using the core philosophies from your books.
            
            Rules for your response:
            1. Adopt the exact tone, vocabulary, and pacing of {author}.
            2. Keep it to a 1-minute read (under 250 words).
            3. Break the advice down into immediate, concrete steps.
            4. Do NOT introduce yourself or say "As {author}". Just start giving the advice.
            5. Use Markdown formatting (bullet points, headers, bold text) to make it highly readable.
            """

        payload = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "system": system_prompt,
            "messages": [
                {
                    "role": "user",
                    "content": f"My problem is: {problem}"
                }
            ]
        }

        response = bedrock.invoke_model(
            modelId='us.anthropic.claude-haiku-4-5-20251001-v1:0', # Or your specific Haiku/Sonnet version
            contentType='application/json',
            accept='application/json',
            body=json.dumps(payload)
        )

        res_body = json.loads(response['body'].read())
        action_plan = res_body['content'][0]['text'].strip()

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({"action_plan": action_plan})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
