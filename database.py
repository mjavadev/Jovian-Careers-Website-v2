from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from JOBS;"))

        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM JOBS WHERE ID = :VAL"),
                              {'VAL': id})
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict()


def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text(
            "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id,:full_name,:email,:linkedin_url,:education,:work_experience,:resume_url)"
        )
        conn.execute(query,
             {
                 'job_id': job_id,
                 'full_name': data['name'],
                 'email': data['mail'],
                 'linkedin_url': data['linkedin'],
                 'education': data['education'],
                 'work_experience': data['work_experience'],
                 'resume_url': data['resume']
             })
        conn.commit() 
