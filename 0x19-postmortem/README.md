# Postmortem Report: Unexpected Nginx Server Crash

## Issue Summary

- **Outage Duration:**  
  1 hour 25 minutes (April 12, 2024, 14:00 - 15:25 UTC+2)

- **Impact:**  
  Our primary website was down, affecting the checkout process for online orders. Approximately 80% of users were unable to complete their purchases, leading to significant user frustration and potential revenue loss.

- **Root Cause:**  
  An unexpected surge in traffic triggered a memory leak in the Nginx server due to a misconfigured caching mechanism, causing the server to crash.

---

## Timeline

- **14:00 UTC+2** - Issue detected by monitoring system alerting on high memory usage.
- **14:02 UTC+2** - On-call engineer receives alert and starts investigation.
- **14:10 UTC+2** - Initial assumption: The issue is related to a recent code deployment.
- **14:20 UTC+2** - Code rollback initiated but did not resolve the issue.
- **14:30 UTC+2** - Misleading investigation: Focus on database performance issues.
- **14:45 UTC+2** - Escalation to senior engineers and DevOps team.
- **15:00 UTC+2** - Memory leak in Nginx identified as the root cause.
- **15:10 UTC+2** - Misconfigured caching mechanism identified as the trigger.
- **15:15 UTC+2** - Caching mechanism disabled, and Nginx server restarted.
- **15:25 UTC+2** - Services restored, and normal operations resumed.

---

## Root Cause and Resolution

### Root Cause
The root cause of the outage was a memory leak in the Nginx server, triggered by a misconfigured caching mechanism. The caching configuration inadvertently allowed for unlimited cache growth, leading to excessive memory consumption. When the server encountered an unexpected surge in traffic, the memory leak intensified, exhausting available memory and causing the server to crash.

### Resolution
The issue was resolved by disabling the faulty caching mechanism and restarting the Nginx server. Once the cache was disabled, memory usage stabilized, and the server was able to handle the incoming traffic without further issues. A thorough review of the Nginx configuration was performed to ensure similar issues would not arise in the future.

---

## Corrective and Preventative Measures

### Improvements and Fixes
- **Review and Update Configuration:** The Nginx caching configuration needs to be reviewed and updated to prevent unbounded cache growth.
- **Traffic Monitoring:** Implement additional monitoring on traffic patterns to identify unexpected surges early.
- **Automated Alerts:** Set up automated alerts for unusual memory usage spikes to catch similar issues before they escalate.

### Tasks
1. **Patch Nginx Configuration:** Modify the caching configuration to limit cache size and implement a cache eviction policy.
2. **Enhanced Monitoring:** Integrate a more robust memory monitoring tool on all web servers.
3. **Stress Testing:** Conduct regular stress tests to simulate traffic surges and identify potential vulnerabilities.
4. **Documentation Update:** Update the internal documentation to include best practices for configuring caching mechanisms in Nginx.
5. **Training:** Provide additional training to the engineering team on identifying and troubleshooting memory leaks.

---

**Final Thoughts**  
While this outage was certainly frustrating, it has provided valuable lessons for our team. By implementing the corrective measures listed above, we aim to prevent such incidents in the future and ensure a smoother, more reliable experience for our users. Plus, we all got to learn the importance of keeping a cool head during a crisis—and maybe that Nginx doesn't always play nicely with infinite memory demands.
