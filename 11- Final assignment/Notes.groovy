

Telecommunication companies routinely gather extensive customer information on a daily basis, 
especially when a customer signs up for their services. 
This customer data typically falls into six main categories:

Details related to customer care services.
Demographic and personal information of customers.
Customer credit scoring data.
Billing and payment records.
Patterns of customer usage.
Information about customer value-added services.

The dataset I'm working with encompasses all of these categories of 
customer data. Each feature will undergo thorough investigation to address 
issues such as null values, duplicates, and outliers. 
Additionally, the distribution of each feature will be analyzed to derive 
actionable insights into customer behavior. These insights will be used to 
provide recommendations to the marketing and customer service teams, 
helping them to formulate effective strategies and focus areas.

1) Customer care service details.
2) Customer demography and personal details.
3) Customer credit score.
4) Bill and payment details.
5) Customer usage pattern.
6) Customer value added services.

'CustomerID': as many values as the entries, dropped
'ServiceArea': to many values and encoding is not know so data are not relevant, we can drop
'Churn': our target, it was an object no-yes, transformed in 0-1

BILL AND PAYMENT DETAILS
    'MonthlyRevenue': had 2 neagtive target and we dropped the entries
                    We have a pick of churning around MonthlyRevenue=30-40, investigate the offers and plans.
                    Customers who pay more are churning in proportion.

    'MonthlyMinutes': the min is zero, there are customers not using it, 671, 1.35% of the cuastomers
                    of these 671, 403 churned, 2.83% of churned customers did not use minutes.
                    I could create a visualisation of churned customer by MonthlyMinutes usage.

    'TotalRecurringCharge': there are negative values, just 5, removed.

    'MonthsInService'

DATA ABOUT CUSTOMER USAGE PATTERN
        'DirectorAssistedCalls': calls made through an operator providing telephone number
        75% is still 0.99 but the max is 159.39. There are some outliers, like only 1 customers
        using it more than 100 times (suspicious activity perhaps??) there are 5378 outliers.

        'OverageMinutes'Overage charges are incurred when a mobile phone (cellphone) is used 
        for more time than the quota fixed under a post-payment plan. There is only one outlier whic I will drop. 
        There are many outliers, the feature is very skewed but circa 30% of outliers 
        also churn, 12.85% of total churned customers. I am not working on these outliers
        because I can see the overage contributes to churn significantly.
        'RoamingCalls'very few customers make roaming calls, there are 36 outliers that I can drop
        // 'PercChangeMinutes' The churn rate among people who decrease the minutes usage is 69.75, I am expecting 
        this feature to have and it is 55% of the churned churned customers!
        'PercChangeRevenues' again very important feature regarding customer behaviour. Churnrate of
        customers their expenditure have increased is 44.04 and they represnt the 31.97% of total churn
        'DroppedCalls' only 29 outliers, I can drop
        'BlockedCalls' not very relevant, thousends of outliers
        'UnansweredCalls' not very relevant, thousends of outliers and churn rate is slightly less than the rate for the whole dataset
        'CustomerCareCalls',
        'ThreewayCalls'
        'ReceivedCalls', 
        'OutboundCalls', 
        'InboundCalls',
        'PeakCallsInOut', 
        'OffPeakCallsInOut', 
        'DroppedBlockedCalls',
        'CallForwardingCalls', 
        'CallWaitingCalls', 
        'UniqueSubs', explored meaning of feature, churn in the outliers is above average
        'ActiveSubs', explored meaning of feture, churn rate is below average
        'ReferralsMadeBySubscriber' more referral does not increase the retention apparently 
        'Handsets', 7.5% of customers with a lot of handsets churn, maybe worth to investigate why they have many handsets and what they do.
        'HandsetPrice'
        'HandsetModels',
        'CurrentEquipmentDays'
CUSTOMER DEMOGRAPHY AND PERSONAL DETAILS
        'AgeHH1'
        'AgeHH2' 
        'ChildrenInHH'
        'Occupation'
        'MaritalStatus'
        'Homeownership'
        'OwnsComputer', 
        'HasCreditCard',
        'TruckOwner', 
        'RVOwner'
        'OwnsMotorcycle'
        'NewCellphoneUser'
        'NotNewCellphoneUser'
        'NonUSTravel'
        'HandsetRefurbished' 
        'HandsetWebCapable'
CUSTOMER CREDIT SCORE
        'IncomeGroup'
        'AdjustmentsToCreditRating'
        'CreditRating'
        'PrizmCode'
 CUSTOMER CARE SERVICE DETAILS
        'RetentionCalls' 
        'MadeCallToRetentionTeam'
        'RetentionOffersAccepted' 
        'BuysViaMailOrder', 
        'RespondsToMailOffers',
        'OptOutMailings'
       
    
        
       