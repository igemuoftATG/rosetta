/* ROSIE Javascript helper functions */

function stringtrim(s)
{
    return s.replace(/^\s+|\s+$/g, '');
}

function share_job(job_path)
{
    r = confirm("Share this job? This will allow access to this page at hard-to-guess URL without need to be logged-in in to ROSIE account");
    if(r) window.location = "/managejob/" + job_path + "/share";
}

function unshare_job(job_path)
{
    r = confirm("Disable sharing for this job?");
    if(r) window.location = "/managejob/" + job_path + "/unshare";
}
