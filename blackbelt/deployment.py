from subprocess import check_call

from blackbelt.handle_github import get_current_branch, run_grunt_in_parallel
from blackbelt.messages import post_message


def deploy_staging():
    branch_name = get_current_branch()

    post_message("Deploying branch %s to staging" % branch_name, "#deploy-queue")

    check_call(['grunt', 'deploy', '--app=apiary-staging', '--force', "--branch=%s" % branch_name])

def deploy_production():
    post_message("Deploying to production", "#deploy-queue")

    slug_creaction_rc = run_grunt_in_parallel((['grunt', 'create-slug'], ['grunt', 'create-slug', '--app=apiary-staging-pre'], ['grunt', 'create-slug', '--app=apiary-staging-qa']))
    if slug_creaction_rc != 0:
		post_message("Slug creation failed, deploy stopped.", "#deploy-queue")
        raise ValueError("One of the slug creations failed. Check output few lines above.")

    check_output(['grunt', 'deploy-slug', '--app=apiary-staging-qa'])
    check_output(['grunt', 'deploy-slug', '--app=apiary-staging-pre'])
    check_output(['grunt', 'deploy-slug'])
