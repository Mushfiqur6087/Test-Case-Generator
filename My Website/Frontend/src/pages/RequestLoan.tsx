import { useState } from "react";
import { FileText, AlertCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { useToast } from "@/hooks/use-toast";
import { MOCK_ACCOUNTS } from "@/lib/mockData";

const collateralAccounts = MOCK_ACCOUNTS.filter(account => 
  account.type === "Checking" || account.type === "Savings"
).map(account => ({
  id: account.id,
  name: `${account.type} Account (${account.accountNumber})`,
  balance: account.balance
}));

const loanTypes = [
  {
    type: "Personal Loan",
    minAmount: 1000,
    maxAmount: 50000,
    interestRate: 7.5,
    term: "12-60 months"
  },
  {
    type: "Auto Loan",
    minAmount: 5000,
    maxAmount: 100000,
    interestRate: 4.5,
    term: "24-84 months"
  },
  {
    type: "Home Loan",
    minAmount: 50000,
    maxAmount: 500000,
    interestRate: 3.5,
    term: "15-30 years"
  }
];

export default function RequestLoan() {
  const [formData, setFormData] = useState({
    loanType: "",
    loanAmount: "",
    downPayment: "",
    collateralAccount: "",
  });
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [isLoading, setIsLoading] = useState(false);
  const { toast } = useToast();

  const selectedLoanType = loanTypes.find(type => type.type === formData.loanType);
  const selectedCollateralAccount = collateralAccounts.find(acc => acc.id === formData.collateralAccount);

  const validateForm = () => {
    const newErrors: Record<string, string> = {};

    // Loan type validation
    if (!formData.loanType) {
      newErrors.loanType = "Please select a loan type";
    }

    // Loan amount validation
    if (!formData.loanAmount || parseFloat(formData.loanAmount) <= 0) {
      newErrors.loanAmount = "Please enter a valid loan amount";
    } else if (selectedLoanType) {
      const amount = parseFloat(formData.loanAmount);
      if (amount < selectedLoanType.minAmount) {
        newErrors.loanAmount = `Minimum loan amount for ${selectedLoanType.type} is $${selectedLoanType.minAmount.toLocaleString()}`;
      } else if (amount > selectedLoanType.maxAmount) {
        newErrors.loanAmount = `Maximum loan amount for ${selectedLoanType.type} is $${selectedLoanType.maxAmount.toLocaleString()}`;
      }
    }

    // Down payment validation
    if (!formData.downPayment || parseFloat(formData.downPayment) <= 0) {
      newErrors.downPayment = "Please enter a valid down payment amount";
    } else if (formData.loanAmount && parseFloat(formData.downPayment) >= parseFloat(formData.loanAmount)) {
      newErrors.downPayment = "Down payment must be less than loan amount";
    }

    // Collateral account validation
    if (!formData.collateralAccount) {
      newErrors.collateralAccount = "Please select a collateral account";
    }

    // Sufficient funds for down payment
    if (selectedCollateralAccount && formData.downPayment && 
        parseFloat(formData.downPayment) > selectedCollateralAccount.balance) {
      newErrors.downPayment = "Insufficient funds in collateral account for down payment";
    }

    // Adequate collateral value (simplified: account balance should be at least 20% of loan amount)
    if (selectedCollateralAccount && formData.loanAmount && 
        selectedCollateralAccount.balance < parseFloat(formData.loanAmount) * 0.2) {
      newErrors.collateralAccount = "Insufficient collateral value (minimum 20% of loan amount required)";
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const simulateCreditUnderwriting = () => {
    // Simplified credit underwriting simulation
    const loanAmount = parseFloat(formData.loanAmount);
    const downPayment = parseFloat(formData.downPayment);
    const downPaymentRatio = downPayment / loanAmount;
    
    // Approval criteria (simplified)
    const hasGoodDownPayment = downPaymentRatio >= 0.1; // At least 10% down
    const reasonableLoanAmount = loanAmount <= 75000; // Reasonable amount
    const randomApproval = Math.random() > 0.2; // 80% approval rate
    
    return hasGoodDownPayment && reasonableLoanAmount && randomApproval;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }

    setIsLoading(true);

    // Simulate loan processing and credit underwriting
    setTimeout(() => {
      const isApproved = simulateCreditUnderwriting();
      
      if (isApproved) {
        const accountNumber = Math.random().toString().substr(2, 9);
        const interestRate = selectedLoanType?.interestRate || 7.5;
        const monthlyPayment = calculateMonthlyPayment(
          parseFloat(formData.loanAmount) - parseFloat(formData.downPayment),
          interestRate,
          60 // 5 years default
        );

        toast({
          title: "Loan approved and created successfully!",
          description: `Account: ****${accountNumber.slice(-4)} | Monthly Payment: $${monthlyPayment.toFixed(2)} | Rate: ${interestRate}%`,
        });

        // Reset form
        setFormData({
          loanType: "",
          loanAmount: "",
          downPayment: "",
          collateralAccount: "",
        });
      } else {
        const denialReasons = [
          "Insufficient credit history",
          "Debt-to-income ratio too high",
          "Inadequate collateral value",
          "Income verification required"
        ];
        const randomReason = denialReasons[Math.floor(Math.random() * denialReasons.length)];
        
        toast({
          title: "Loan application denied",
          description: `Reason: ${randomReason}. Please contact our loan officer for assistance.`,
          variant: "destructive",
        });
      }
      
      setIsLoading(false);
    }, 2000);
  };

  const calculateMonthlyPayment = (principal: number, annualRate: number, months: number) => {
    const monthlyRate = annualRate / 100 / 12;
    return (principal * monthlyRate * Math.pow(1 + monthlyRate, months)) / 
           (Math.pow(1 + monthlyRate, months) - 1);
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
    
    if (errors[name]) {
      setErrors({
        ...errors,
        [name]: "",
      });
    }
  };

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
    }).format(amount);
  };

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <div className="text-center">
        <FileText className="h-12 w-12 text-primary mx-auto mb-4" />
        <h1 className="text-3xl font-bold text-foreground">Request Loan</h1>
        <p className="text-muted-foreground">Apply for a loan to meet your financial needs</p>
      </div>

      {/* Loan Type Selection */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {loanTypes.map((loanType) => (
          <Card 
            key={loanType.type}
            className={`cursor-pointer transition-all border-2 ${
              formData.loanType === loanType.type 
                ? "border-primary bg-primary/5" 
                : "border-border hover:border-primary/50"
            }`}
            onClick={() => setFormData({ ...formData, loanType: loanType.type })}
          >
            <CardHeader>
              <CardTitle className="flex items-center justify-between text-sm">
                {loanType.type}
                <input
                  type="radio"
                  checked={formData.loanType === loanType.type}
                  onChange={() => {}}
                  className="text-primary"
                />
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-2 text-sm">
                <p><strong>Rate:</strong> {loanType.interestRate}% APR</p>
                <p><strong>Amount:</strong> ${loanType.minAmount.toLocaleString()} - ${loanType.maxAmount.toLocaleString()}</p>
                <p><strong>Term:</strong> {loanType.term}</p>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Loan Application Form */}
      <Card>
        <CardHeader>
          <CardTitle>Loan Application</CardTitle>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-6">
            {/* Loan Amount */}
            <div className="space-y-2">
              <Label htmlFor="loanAmount">Loan Amount</Label>
              <div className="relative">
                <span className="absolute left-3 top-1/2 transform -translate-y-1/2 text-muted-foreground">$</span>
                <Input
                  id="loanAmount"
                  name="loanAmount"
                  type="number"
                  step="100"
                  min="100"
                  required
                  value={formData.loanAmount}
                  onChange={handleInputChange}
                  placeholder="0.00"
                  className={`pl-8 ${errors.loanAmount ? "border-destructive" : ""}`}
                  disabled={!formData.loanType}
                />
              </div>
              {selectedLoanType && (
                <p className="text-sm text-muted-foreground">
                  Range: ${selectedLoanType.minAmount.toLocaleString()} - ${selectedLoanType.maxAmount.toLocaleString()}
                </p>
              )}
              {errors.loanAmount && (
                <p className="text-sm text-destructive">{errors.loanAmount}</p>
              )}
            </div>

            {/* Down Payment */}
            <div className="space-y-2">
              <Label htmlFor="downPayment">Down Payment Amount</Label>
              <div className="relative">
                <span className="absolute left-3 top-1/2 transform -translate-y-1/2 text-muted-foreground">$</span>
                <Input
                  id="downPayment"
                  name="downPayment"
                  type="number"
                  step="100"
                  min="100"
                  required
                  value={formData.downPayment}
                  onChange={handleInputChange}
                  placeholder="0.00"
                  className={`pl-8 ${errors.downPayment ? "border-destructive" : ""}`}
                  disabled={!formData.loanType}
                />
              </div>
              {errors.downPayment && (
                <p className="text-sm text-destructive">{errors.downPayment}</p>
              )}
            </div>

            {/* Collateral Account */}
            <div className="space-y-2">
              <Label htmlFor="collateralAccount">Collateral Account</Label>
              <Select 
                onValueChange={(value) => setFormData({ ...formData, collateralAccount: value })}
                disabled={!formData.loanType}
              >
                <SelectTrigger className={errors.collateralAccount ? "border-destructive" : ""}>
                  <SelectValue placeholder="Select collateral account" />
                </SelectTrigger>
                <SelectContent>
                  {collateralAccounts.map((account) => (
                    <SelectItem key={account.id} value={account.id}>
                      <div className="flex justify-between items-center w-full">
                        <span>{account.name}</span>
                        <span className="text-muted-foreground ml-4">
                          {formatCurrency(account.balance)}
                        </span>
                      </div>
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
              {selectedCollateralAccount && (
                <p className="text-sm text-muted-foreground">
                  Available balance: {formatCurrency(selectedCollateralAccount.balance)}
                </p>
              )}
              {errors.collateralAccount && (
                <p className="text-sm text-destructive">{errors.collateralAccount}</p>
              )}
            </div>

            {/* Loan Processing Information */}
            <Alert>
              <AlertCircle className="h-4 w-4" />
              <AlertDescription>
                Loan applications are subject to credit approval. Processing may take 1-3 business days. 
                Your collateral account will be evaluated for adequate coverage.
              </AlertDescription>
            </Alert>

            {/* Submit Button */}
            <Button
              type="submit"
              className="w-full bg-primary hover:bg-primary-hover"
              disabled={isLoading || !formData.loanType}
            >
              {isLoading ? "Processing Application..." : "Apply for Loan"}
            </Button>
          </form>
        </CardContent>
      </Card>

      {/* Application Summary */}
      {formData.loanAmount && formData.downPayment && formData.collateralAccount && selectedLoanType && (
        <Card>
          <CardHeader>
            <CardTitle>Application Summary</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              <div className="flex justify-between">
                <span className="text-muted-foreground">Loan Type:</span>
                <span className="font-semibold">{formData.loanType}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-muted-foreground">Requested Amount:</span>
                <span className="font-semibold">{formatCurrency(parseFloat(formData.loanAmount) || 0)}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-muted-foreground">Down Payment:</span>
                <span className="font-semibold">{formatCurrency(parseFloat(formData.downPayment) || 0)}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-muted-foreground">Net Loan Amount:</span>
                <span className="font-semibold">
                  {formatCurrency((parseFloat(formData.loanAmount) || 0) - (parseFloat(formData.downPayment) || 0))}
                </span>
              </div>
              <div className="flex justify-between">
                <span className="text-muted-foreground">Interest Rate:</span>
                <span>{selectedLoanType.interestRate}% APR</span>
              </div>
              <div className="flex justify-between">
                <span className="text-muted-foreground">Collateral Account:</span>
                <span>{collateralAccounts.find(acc => acc.id === formData.collateralAccount)?.name}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-muted-foreground">Processing Time:</span>
                <span>1-3 business days</span>
              </div>
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
